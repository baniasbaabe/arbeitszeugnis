import os

import fitz
import google.generativeai as genai
import PIL.Image
import streamlit as st
from dotenv import load_dotenv

from src.display_results import find_matches, render_displacy
from src.model_constants import ModelName
from src.prompts import JOB_REFERENCE_DECODER_PROMPT
from src.utils import clean_results, remove_images

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
load_dotenv()
job_reference_content = ""
images = []
model = genai.GenerativeModel(ModelName.GEMINI_PRO.value)

st.set_page_config(
    page_title="Arbeitszeugnis.ai",
    page_icon="https://1000logos.net/wp-content/uploads/2023/11/Brain-Emoji.png",
)

st.title("🧠 Arbeitszeugnis.ai")

file_path = st.file_uploader("Upload your Job Reference")


if file_path:
    with st.spinner("Your Job Reference will be decoded. Hold on..."):
        doc = fitz.open(stream=file_path.read(), filetype="pdf")

        for i, page in enumerate(doc):
            pix = page.get_pixmap()
            pix.save(f"page_{i}.png")
            images.append(f"page_{i}.png")

        for image in images:
            try:
                file = PIL.Image.open(image)
                job_reference_content += model.generate_content(
                    ["Extract the text from the image", file]
                ).text
            except Exception:
                st.error(
                    "API Connection Error: Please check if your country is eligible for the API https://ai.google.dev/available_regions. Or Gemini Pro API isn't free anymore :)"
                )
                st.stop()

        prompt = JOB_REFERENCE_DECODER_PROMPT + job_reference_content
        results = model.generate_content(prompt).text
        results = clean_results(results)

        reference_sents = find_matches(results, job_reference_content)

        dep_svg = render_displacy(job_reference_content, reference_sents)
        st.markdown(dep_svg, unsafe_allow_html=True)

        remove_images(images)

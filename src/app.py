import fitz
import streamlit as st
from dotenv import load_dotenv
from litellm.exceptions import APIConnectionError

from src.content import Content
from src.display_results import find_matches, render_displacy
from src.model_constants import ModelName
from src.prompts import JOB_REFERENCE_DECODER_PROMPT, TEXT_EXTRACTION_PROMPT
from src.response_generation import generate_response
from src.utils import clean_results, remove_images

load_dotenv()
job_reference_content = ""
images = []

st.set_page_config(page_title="Arbeitszeugnis.ai", page_icon="https://1000logos.net/wp-content/uploads/2023/11/Brain-Emoji.png")

st.title("🧠 Arbeitszeugnis.ai")

file_path = st.file_uploader("Upload your job reference")

if file_path:
    
    doc = fitz.open(stream = file_path.read(), filetype="pdf")
    
    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        pix.save(f"page_{i}.png")
        images.append(f"page_{i}.png")
    
    for image in images:
        try:
            job_reference_content += generate_response(ModelName.GEMINI_VISION, Content(TEXT_EXTRACTION_PROMPT, image))
        except APIConnectionError:
            st.error("API Connection Error: Please check if your country is eligible for the API https://ai.google.dev/available_regions.")
            st.stop()

    JOB_REFERENCE_DECODER_PROMPT = JOB_REFERENCE_DECODER_PROMPT + job_reference_content
    results = generate_response(ModelName.GEMINI_PRO, Content(JOB_REFERENCE_DECODER_PROMPT))
    results = clean_results(results)
    
    reference_sents = find_matches(results, job_reference_content)
    
    dep_svg = render_displacy(job_reference_content, reference_sents)
    st.markdown(dep_svg, unsafe_allow_html=True)
    
    remove_images(images)
from prompts import TEXT_EXTRACTION_PROMPT, JOB_REFERENCE_DECODER_PROMPT
from content import Content
from model_constants import ModelName
from response_generation import generate_response
import streamlit as st
from dotenv import load_dotenv
import fitz

load_dotenv()

st.title("Arbeitszeugnis")

file_path = st.file_uploader("Upload your job reference")

job_reference_content = ""

if file_path:
    
    doc = fitz.open(stream = file_path.read(), filetype="pdf")
    images = []
    
    for i, page in enumerate(doc):
        pix = page.get_pixmap()  # render page to an image
        pix.save(f"page_{i}.png")
        images.append(f"page_{i}.png")
    
    for image in images:
        job_reference_content += generate_response(ModelName.GEMINI_VISION, Content(TEXT_EXTRACTION_PROMPT, image))

        st.write(job_reference_content)

    JOB_REFERENCE_DECODER_PROMPT = JOB_REFERENCE_DECODER_PROMPT + job_reference_content
    results = generate_response(ModelName.GEMINI_PRO, Content(JOB_REFERENCE_DECODER_PROMPT))

    st.write(results)
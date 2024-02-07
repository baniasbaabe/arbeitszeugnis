from prompts import TEXT_EXTRACTION_PROMPT, JOB_REFERENCE_DECODER_PROMPT
from content import Content
from model_constants import ModelName
from response_generation import generate_response
import streamlit as st
from dotenv import load_dotenv
import fitz
import os
from litellm.exceptions import APIConnectionError
from spacy import displacy
from ast import literal_eval
import re

load_dotenv()

st.title("🧠 Arbeitszeugnis.ai")

file_path = st.file_uploader("Upload your job reference")

job_reference_content = ""

reference_sents = []

colors = {}

if file_path:
    
    doc = fitz.open(stream = file_path.read(), filetype="pdf")
    images = []
    
    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        pix.save(f"page_{i}.png")
        images.append(f"page_{i}.png")
    
    for image in images:
        try:
            job_reference_content += generate_response(ModelName.GEMINI_VISION, Content(TEXT_EXTRACTION_PROMPT, image))
        except APIConnectionError:
            st.error("API Connection Error: Please check if your country is eligible for the API. If you are in an eligible country, please check your API key.")
            st.stop()

    JOB_REFERENCE_DECODER_PROMPT = JOB_REFERENCE_DECODER_PROMPT + job_reference_content
    results = generate_response(ModelName.GEMINI_PRO, Content(JOB_REFERENCE_DECODER_PROMPT))
    
    results = results.replace("```json", "")
    results = results.replace("```JSON", "")
    results = results.replace("```", "")	
    results = literal_eval(results)


    for entry in results:
        for match in re.finditer(entry["satz_aus_text"], job_reference_content):
            reference_sents.append({"start":match.start(), "end":match.end(), "label":f"{entry['kategorie']}, Note: {entry['note']}"})

    dic_ents = {
        "text": job_reference_content,
        "ents": reference_sents,
        "title": None
    }
    dep_svg = displacy.render(dic_ents, style="ent", jupyter=False, manual=True)
    st.markdown(dep_svg, unsafe_allow_html=True)        
        
    for image in images:
        os.remove(image)
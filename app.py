import streamlit as st
import fitz
import numpy as np
import re
import easyocr
import pandas as pd
import re
import string
import nltk
import spacy
nltk.download("punkt")
nltk.download("stopwords")
from nltk.tokenize import word_tokenize
from PIL import Image
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import TextClassificationPipeline
from spacy import displacy

my_stops = ['aber',
 'alle',
 'allem',
 'allen',
 'aller',
 'alles',
 'als',
 'also',
 'am',
 'an',
 'ander',
 'andere',
 'anderem',
 'anderen',
 'anderer',
 'anderes',
 'anderm',
 'andern',
 'anderr',
 'anders',
 'auch',
 'auf',
 'aus',
 'bei',
 'bin',
 'bis',
 'bist',
 'da',
 'damit',
 'dann',
 'der',
 'den',
 'des',
 'dem',
 'die',
 'das',
 'dass',
 'daß',
 'derselbe',
 'derselben',
 'denselben',
 'desselben',
 'demselben',
 'dieselbe',
 'dieselben',
 'dasselbe',
 'dazu',
 'dein',
 'deine',
 'deinem',
 'deinen',
 'deiner',
 'deines',
 'denn',
 'derer',
 'dessen',
 'dich',
 'dir',
 'du',
 'dies',
 'diese',
 'diesem',
 'diesen',
 'dieser',
 'dieses',
 'doch',
 'dort',
 'durch',
 'ein',
 'eine',
 'einem',
 'einen',
 'einer',
 'eines',
 'einig',
 'einige',
 'einigem',
 'einigen',
 'einiger',
 'einiges',
 'einmal',
 'er',
 'ihn',
 'ihm',
 'es',
 'etwas',
 'euer',
 'eure',
 'eurem',
 'euren',
 'eurer',
 'eures',
 'für',
 'gegen',
 'gewesen',
 'hab',
 'habe',
 'haben',
 'hat',
 'hatte',
 'hatten',
 'hier',
 'hin',
 'hinter',
 'ich',
 'mich',
 'mir',
 'ihr',
 'ihre',
 'ihrem',
 'ihren',
 'ihrer',
 'ihres',
 'euch',
 'im',
 'in',
 'indem',
 'ins',
 'ist',
 'jede',
 'jedem',
 'jeden',
 'jeder',
 'jedes',
 'jene',
 'jenem',
 'jenen',
 'jener',
 'jenes',
 'jetzt',
 'kann',
 'kein',
 'keine',
 'keinem',
 'keinen',
 'keiner',
 'keines',
 'können',
 'könnte',
 'machen',
 'man',
 'manche',
 'manchem',
 'manchen',
 'mancher',
 'manches',
 'mein',
 'meine',
 'meinem',
 'meinen',
 'meiner',
 'meines',
 'mit',
 'muss',
 'musste',
 'nach',
 'nicht',
 'nichts',
 'noch',
 'nun',
 'nur',
 'ob',
 'oder',
 'ohne',
 'sein',
 'seine',
 'seinem',
 'seinen',
 'seiner',
 'seines',
 'selbst',
 'sich',
 'sie',
 'ihnen',
 'sind',
 'so',
 'solche',
 'solchem',
 'solchen',
 'solcher',
 'solches',
 'soll',
 'sollte',
 'sondern',
 'sonst',
 'über',
 'um',
 'und',
 'uns',
 'unsere',
 'unserem',
 'unseren',
 'unser',
 'unseres',
 'unter',
 'vom',
 'von',
 'vor',
 'während',
 'war',
 'waren',
 'warst',
 'was',
 'weg',
 'weil',
 'weiter',
 'welche',
 'welchem',
 'welchen',
 'welcher',
 'welches',
 'wenn',
 'werde',
 'werden',
 'wie',
 'wieder',
 'will',
 'wir',
 'wird',
 'wirst',
 'wo',
 'wollen',
 'wollte',
 'würde',
 'würden',
 'zu',
 'zum',
 'zur',
 'zwar',
 'zwischen']
nlp = spacy.load('de_core_news_sm')

def preprocess_text(text):
  # text = text.lower()
  sent_text = nltk.sent_tokenize(text)
  sentences = []
  for sent in sent_text:
    tokens = word_tokenize(sent)
    no_stops = [word for word in tokens if word.lower() not in my_stops]
    sent = " ".join(no_stops)
    sentences.append(sent)
  text = ' '.join(sentences)
  text = text.translate(
        str.maketrans("", "", string.punctuation + string.digits)
    )  
  doc = nlp(text)  
  people = [e.text for e in doc.ents if e.label_ in ['PER']]
  regex = re.compile('|'.join(people))
  text = re.sub(regex, '', text) 
  # doc = nlp(text)
  # text = ' '.join([x.lemma_ for x in doc])
  return text


OUTPUT_TO_LABEL_CRIT = {"LABEL_0":'Arbeitsergebnis', "LABEL_1":'Arbeitsweise', "LABEL_2":'Belastbarkeit', "LABEL_3":'Fachwissen',
       "LABEL_4":'Fuehrungsstil', "LABEL_5":'Gesamturteil', "LABEL_6":'Irrelevant',
       "LABEL_7":'Leistungsbereitschaft', "LABEL_8":'Schlussformulierung', "LABEL_9":'Verhalten'}

OUTPUT_TO_LABEL_GRADE = {
    "LABEL_0": 1.0, "LABEL_1":2.0, "LABEL_2":3.0, "LABEL_3":4.0, "LABEL_4":5.0, "LABEL_5":6.0, "LABEL_6":99
}

def app():
    st.set_page_config(
     page_title="arbeitszeugnis.ai",
     page_icon="🧠",
 )
    hide_streamlit_style = """
                    <style>
                    div[data-testid="stToolbar"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    div[data-testid="stDecoration"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    div[data-testid="stStatusWidget"] {
                    visibility: hidden;
                    height: 0%;
                    position: fixed;
                    }
                    #MainMenu {
                    visibility: hidden;
                    height: 0%;
                    }
                    header {
                    visibility: hidden;
                    height: 0%;
                    }
                    footer {
                    visibility: hidden;
                    height: 0%;
                    }
                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.markdown("<h1 style='text-align: center; color: #36454F;'>📜 arbeitszeugnis.ai 📜</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #36454F;'>🧠Lass die KI die Codes deines Arbeitszeugnisses entschlüsseln</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(label="Lade dein Arbeitszeugnis hoch", type=["pdf"])
    print(uploaded_file)
    if not uploaded_file:
        return

    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

    doc = fitz.open(stream = uploaded_file.read(), filetype="pdf")  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(matrix=mat, dpi=800)  # render page to an image
        pix.save("page-%i.png" % page.number)  # store image as a PNG
        break
    print("Converted pdf to png")
    doc.close()

    img = Image.open("page-0.png")
    print("Read png")
    img = np.array(img)
    print("Converted to array")

    eng_reader = easyocr.Reader(['de'])
    detected_text = eng_reader.readtext(img, paragraph = True)
    print("Detected text")

    tokenizer = AutoTokenizer.from_pretrained("bert-base-german-cased")
    model_note = AutoModelForSequenceClassification.from_pretrained("models/model_grade", num_labels=7)
    model_kriterium = AutoModelForSequenceClassification.from_pretrained("models/model_criteria", num_labels=10)
    pipe_note = TextClassificationPipeline(model=model_note, tokenizer=tokenizer, return_all_scores=True)
    pipe_kriterium = TextClassificationPipeline(model=model_kriterium, tokenizer=tokenizer, return_all_scores=True)

    def get_prediction(text):
        text = preprocess_text(text)
        
        pred_kriterium = pipe_kriterium(text)
        pred_kriterium = sorted(pred_kriterium[0], key=lambda item: item["score"], reverse=True)

        pred_note = pipe_note(text)
        pred_note = sorted(pred_note[0], key=lambda item: item["score"], reverse=True)

        return {"kriterium": pred_kriterium[0]["label"], "note": pred_note[0]["label"]}
    
    reference_sents = []
    full_text = ""

    for text in detected_text:
        t = text[-1]
        sentences = nltk.sent_tokenize(t)
        for s in sentences:
            labels = get_prediction(s)
            raw_label_kriterium = labels["kriterium"]
            raw_label_note = labels["note"]
            kriterium_label = OUTPUT_TO_LABEL_CRIT[raw_label_kriterium]
            note_label = OUTPUT_TO_LABEL_GRADE[raw_label_note]

            if kriterium_label == "Irrelevant" or note_label == 99:
                continue
            
            full_text += s

            for match in re.finditer(s, full_text):
                reference_sents.append({"start":match.start(), "end":match.end(), "label":f"{kriterium_label}, {note_label}"})
    print("Ausgaben ")
    dic_ents = {
        "text": full_text,
        "ents": reference_sents,
        "title": None
    }
    dep_svg = displacy.render(dic_ents, style="ent", jupyter=False, manual=True)
    st.markdown(dep_svg, unsafe_allow_html=True)
    print("Render complete")

if __name__ == "__main__":
    app()
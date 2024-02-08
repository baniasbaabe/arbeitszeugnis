import re
from spacy import displacy

def find_matches(results, job_reference_content):
    reference_sents = []
    for entry in results:
        for match in re.finditer(entry["satz_aus_text"], job_reference_content):
            reference_sents.append({"start":match.start(), "end":match.end(), "label":f"{entry['kategorie']}, Note: {entry['note']}"})
    return reference_sents


def render_displacy(job_reference_content, reference_sents):
    dic_ents = {
        "text": job_reference_content,
        "ents": reference_sents,
        "title": None
    }
    return displacy.render(dic_ents, style="ent", jupyter=False, manual=True)
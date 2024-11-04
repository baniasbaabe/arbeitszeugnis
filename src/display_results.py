import re
from typing import List

from spacy import displacy


def find_matches(results: List[dict], job_reference_content: str) -> List[dict]:
    """
    For every result from the job reference decoder, find matches in the job reference content.
    Needed for displacy rendering.

    Args:
        results (List[dict]): Results from Gemini Pro API.
        job_reference_content (str): Whole job reference content.

    Returns:
        List[dict]: List of matches with start, end and label for displacy.
    """
    reference_sents = []
    for entry in results:
        for match in re.finditer(entry["satz_aus_text"], job_reference_content):
            reference_sents.append(
                {
                    "start": match.start(),
                    "end": match.end(),
                    "label": f"{entry['kategorie']}, Note: {entry['note']}",
                }
            )
    return reference_sents


def render_displacy(job_reference_content: str, reference_sents: List[dict]) -> str:
    """
    Render displacy SVG for the job reference content.

    Args:
        job_reference_content (str): Whole job reference content.
        reference_sents (List[dict]): Start, end and label for displacy.

    Returns:
        str: Displacy SVG.
    """
    dic_ents = {"text": job_reference_content, "ents": reference_sents, "title": None}
    return displacy.render(dic_ents, style="ent", jupyter=False, manual=True)

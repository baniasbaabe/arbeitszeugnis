import os
from ast import literal_eval
from typing import List


def remove_images(images: List[str]) -> None:
    """
    Remove images which are created from PDFs to feed to Gemini Vision API.

    Args:
        images (List[str]): List of image paths.
    """
    for image in images:
        os.remove(image)
    
def clean_results(results: str) -> List[dict]:
    """
    Clean up results from Gemini Pro API.

    Args:
        results (str): Raw results from Gemini Pro API.

    Returns:
        List[dict]: Cleaned up results without noise.
    """
    results = results.replace("```json", "")
    results = results.replace("```JSON", "")
    results = results.replace("```", "")	
    results = literal_eval(results)
    return results
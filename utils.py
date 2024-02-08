import os 
from ast import literal_eval

def remove_images(images):
    for image in images:
        os.remove(image)
    
def clean_results(results):
    results = results.replace("```json", "")
    results = results.replace("```JSON", "")
    results = results.replace("```", "")	
    results = literal_eval(results)
    return results
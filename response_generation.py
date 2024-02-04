import litellm
from model_constants import ModelName
from content import Content

def generate_response(model_name: ModelName, content: Content):
    response = litellm.completion(
    model=model_name.value,
    messages=[{
        "role": "user",
        "content": content.to_dict()
               }],
    )

    content = response.get('choices', [{}])[0].get('message', {}).get('content')
    
    return content
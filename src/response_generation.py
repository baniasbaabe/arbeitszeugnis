import litellm

from content import Content
from model_constants import ModelName


def generate_response(model_name: ModelName, content: Content) -> str:
    """
    Generate response from the model (Pro or Vision).

    Args:
        model_name (ModelName): Pro or Vision model
        content (Content): The prompt and file path if available.

    Returns:
        str: Response from the model.
    """
    response = litellm.completion(
    model=model_name.value,
    messages=[{
        "role": "user",
        "content": content.to_list_of_dict()
               }],
    )

    content = response.get('choices', [{}])[0].get('message', {}).get('content')
    
    return content
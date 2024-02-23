import pytest
from unittest.mock import patch
from src.response_generation import generate_response
from src.model_constants import ModelName 
from src.content import Content


@pytest.mark.parametrize("model_name", [ModelName.GEMINI_PRO, ModelName.GEMINI_VISION])
def test_generate_response(model_name):
    with patch('litellm.completion') as mock_completion:
        test_content = Content("Your test prompt", "file_path_if_available.png")

        mock_completion.return_value = {
            'choices': [{
                'message': {'content': 'Mocked response content'}
            }]
        }

        result = generate_response(model_name, test_content)

        mock_completion.assert_called_once_with(
            model=model_name.value,
            messages=[{
                "role": "user",
                "content": test_content.to_list_of_dict()
            }]
        )

        assert result == 'Mocked response content'

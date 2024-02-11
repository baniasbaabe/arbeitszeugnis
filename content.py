from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class Content:
    """
    Data class for the content inserted to Gemini API.
    """
    prompt: str
    file_path: Optional[Any] = None
    
    def to_list_of_dict(self) -> List[dict]:
        result = [{
            "type": "text",
            "text": self.prompt
        }]

        if self.file_path is not None:
            result.append(
                {
                    "type": "image_url",
                    "image_url": {"url": self.file_path}
                }
            )

        return result
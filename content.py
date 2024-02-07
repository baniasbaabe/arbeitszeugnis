from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Content:
    prompt: str
    file_path: Optional[Any] = None
    
    def to_dict(self):
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
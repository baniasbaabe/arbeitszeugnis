from dataclasses import dataclass
from typing import Optional

@dataclass
class Content:
    prompt: str
    image_path: Optional[str] = None
    
    def to_dict(self):
        result = {
            "type": "text",
            "text": self.prompt
        }

        if self.image_path is not None:
            result["type"] = "image"
            result["image"] = self.image_path

        return result
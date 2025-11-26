from pydantic import BaseModel
from typing import Dict, Optional

class GenerateRequest(BaseModel):
    prompt: str

class AnalyzeRequest(BaseModel):
    image: str

class APIResponse(BaseModel):
    request_id: str
    generated_image: Optional[str] = None
    clip_analysis: Dict
    basic_segmentation: Dict
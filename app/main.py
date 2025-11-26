import uuid
import torch
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from app.schemas import GenerateRequest, AnalyzeRequest, APIResponse
from app.services.sd_service import SDService
from app.services.clip_service import CLIPService
from app.services.sam_service import SAMService
from app.utils import encode_image_to_base64, decode_base64_to_image

models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Running on: {device}")
    models["sd"] = SDService(device)
    models["clip"] = CLIPService(device)
    models["sam"] = SAMService(device)
    yield
    models.clear()

app = FastAPI(title="Text-to-Image Pipeline", lifespan=lifespan)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.post("/generate", response_model=APIResponse)
async def generate_image(request: GenerateRequest):
    try:
        image = models["sd"].generate(request.prompt)
        clip_result = models["clip"].analyze(image)
        sam_result = models["sam"].segment(image)
        
        return APIResponse(
            request_id=str(uuid.uuid4()),
            generated_image=encode_image_to_base64(image),
            clip_analysis=clip_result,
            basic_segmentation=sam_result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze", response_model=APIResponse)
async def analyze_image(request: AnalyzeRequest):
    try:
        image = decode_base64_to_image(request.image)
        clip_result = models["clip"].analyze(image)
        sam_result = models["sam"].segment(image)
        
        return APIResponse(
            request_id=str(uuid.uuid4()),
            clip_analysis=clip_result,
            basic_segmentation=sam_result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
import torch
from diffusers import StableDiffusionPipeline

class SDService:
    def __init__(self, device):
        self.device = device
        print("Loading Stable Diffusion...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", 
            torch_dtype=torch.float32  # Use float32 for CPU safety
        )
        self.pipe.to(self.device)
        self.pipe.enable_attention_slicing()

    def generate(self, prompt: str):
        # SPEED FIX: num_inference_steps=5 makes it fast on CPU
        steps = 5 if self.device == "cpu" else 50
        return self.pipe(prompt, num_inference_steps=steps).images[0]
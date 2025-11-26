import torch
from transformers import CLIPProcessor, CLIPModel

class CLIPService:
    def __init__(self, device):
        self.device = device
        print("Loading CLIP...")
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        # Standard concepts to check against
        self.concepts = ["landscape", "portrait", "animal", "technology", "food", "art", "person", "object"]

    def analyze(self, image):
        inputs = self.processor(text=self.concepts, images=image, return_tensors="pt", padding=True).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        probs = outputs.logits_per_image.softmax(dim=1).cpu().numpy()[0]
        
        scores = {concept: float(prob) for concept, prob in zip(self.concepts, probs)}
        # Sort by confidence
        sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
        
        return {
            "concepts": list(sorted_scores.keys())[:3], # Top 3
            "confidence_scores": sorted_scores
        }
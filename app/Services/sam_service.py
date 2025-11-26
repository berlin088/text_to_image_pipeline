import torch
import numpy as np
import os
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor
from app.utils import polygon_from_mask

class SAMService:
    def __init__(self, device):
        self.device = device
        print("Loading SAM2...")
        checkpoint = "./checkpoints/sam2_hiera_small.pt"
        model_cfg = "sam2_hiera_s.yaml"
        
        if os.path.exists(checkpoint):
            try:
                self.sam_model = build_sam2(model_cfg, checkpoint, device=device)
                self.predictor = SAM2ImagePredictor(self.sam_model)
            except Exception as e:
                print(f"SAM2 Error: {e}")
                self.predictor = None
        else:
            print("WARNING: SAM2 Checkpoint missing. Segmentation will be skipped.")
            self.predictor = None

    def segment(self, image):
        if not self.predictor:
            return {"masks": [], "polygons": []}

        img_np = np.array(image)
        self.predictor.set_image(img_np)
        
        # Segment center point
        h, w = img_np.shape[:2]
        input_point = np.array([[w//2, h//2]])
        input_label = np.array([1])

        masks, _, _ = self.predictor.predict(
            point_coords=input_point,
            point_labels=input_label,
            multimask_output=False,
        )
        polygon = polygon_from_mask(masks[0].astype(bool))
        return {"masks": [], "polygons": [polygon]}
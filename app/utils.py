import base64
from io import BytesIO
from PIL import Image
import numpy as np

def encode_image_to_base64(image: Image.Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def decode_base64_to_image(base64_str: str) -> Image.Image:
    return Image.open(BytesIO(base64.b64decode(base64_str))).convert("RGB")

def polygon_from_mask(mask: np.ndarray):
    rows, cols = np.where(mask)
    if len(rows) > 0:
        return [[int(cols.min()), int(rows.min())], [int(cols.max()), int(rows.max())]]
    return []
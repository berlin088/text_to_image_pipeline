import requests
import base64
import json
import os

API_URL = "http://127.0.0.1:8000/generate"
OUTPUT_DIR = "example_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)
print("Requesting image generation...")

try:
    response = requests.post(API_URL, json={"prompt": "a futuristic city"}, timeout=300)
    if response.status_code == 200:
        data = response.json()
        
        # Save Image
        img_data = base64.b64decode(data["generated_image"])
        with open(f"{OUTPUT_DIR}/result.png", "wb") as f:
            f.write(img_data)
            
        # Save JSON Response
        with open(f"{OUTPUT_DIR}/response.json", "w") as f:
            json.dump(data, f, indent=2)
            
        print(f"Success! Check the '{OUTPUT_DIR}' folder.")
    else:
        print("Error:", response.text)
except Exception as e:
    print("Failed:", e)
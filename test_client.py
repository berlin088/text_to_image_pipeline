import requests
import base64
import json
import os

# Configuration
API_URL = "http://127.0.0.1:8000/generate"
OUTPUT_DIR = "example_outputs"
PROMPT = "a cyberpunk cat wearing sunglasses"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"Sending request to {API_URL}...")
print(f"Prompt: '{PROMPT}'")
print("Waiting for AI... (This can take 1-2 minutes on CPU)")

try:
    # Send the request to your running server
    response = requests.post(API_URL, json={"prompt": PROMPT}, timeout=300)
    
    if response.status_code == 200:
        data = response.json()
        
        # 1. Save the Image
        image_data = base64.b64decode(data["generated_image"])
        image_path = os.path.join(OUTPUT_DIR, "result.png")
        with open(image_path, "wb") as f:
            f.write(image_data)
            
        # 2. Save the Analysis data
        json_path = os.path.join(OUTPUT_DIR, "response.json")
        with open(json_path, "w") as f:
            json.dump(data, f, indent=2)
            
        print("\n✅ SUCCESS!")
        print(f"1. Image saved to: {image_path}")
        print(f"2. Data saved to:  {json_path}")
        print("Go open the 'example_outputs' folder to see your image!")
        
    else:
        print(f"❌ Error from server: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ Connection Failed: {e}")
    print("Make sure run.py is running in a SEPARATE terminal!")
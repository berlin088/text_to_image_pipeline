# 🎨 Text-to-Image Generation Pipeline with Multi-Model Analysis

A comprehensive AI pipeline that generates images from text using **Stable Diffusion**, analyzes them using **CLIP**, and performs instance segmentation using **Meta's Segment Anything Model 2 (SAM2)**.

The system exposes a robust **FastAPI** interface capable of running on both **GPU** (for speed) and **CPU** (compatibility).

## 🚀 Features

* **Text-to-Image Generation**: Uses Stable Diffusion v1.5 to create high-quality images from text prompts.
* **Image Analysis**: Uses CLIP to classify concepts within the generated image and provide confidence scores.
* **Instance Segmentation**: Uses SAM2 (Segment Anything Model 2) to auto-detect and segment objects.
* **RESTful API**: Fully documented API endpoints built with FastAPI.
* **Docker Support**: Containerized for easy deployment.

---

## 📂 Project Structure

```text
text_to_image_pipeline/
├── app/
│   ├── services/           # AI Model Logic (SD, CLIP, SAM2)
│   ├── main.py             # API Entry Point
│   ├── schemas.py          # Pydantic Models
│   └── utils.py            # Image Processing Helpers
├── checkpoints/            # Model Weights (Download SAM2 here)
├── example_outputs/        # Generated images and JSON results
├── Dockerfile              # Docker Configuration
├── requirements.txt        # Python Dependencies
├── run.py                  # Server Startup Script
└── test_client.py          # Testing Script
🛠️ Installation (Local)
1. Prerequisites
Python 3.10 or higher

Git installed

2. Setup Virtual Environment
Bash

# Clone the repository
git clone <YOUR_REPO_URL>
cd text_to_image_pipeline

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
3. Install Dependencies
Bash

# Install PyTorch (CPU Version)
pip install torch torchvision --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu)

# If you have an NVIDIA GPU, use this instead:
# pip install torch torchvision --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)

# Install Project Requirements
pip install -r requirements.txt

# Install SAM2 from Source
pip install git+[https://github.com/facebookresearch/segment-anything-2.git](https://github.com/facebookresearch/segment-anything-2.git)
4. ⚠️ Download Model Weights (Required)
You must manually download the SAM2 model checkpoint.

Download Link: sam2_hiera_small.pt

Action: Move the file into the checkpoints/ folder.

Path: text_to_image_pipeline/checkpoints/sam2_hiera_small.pt

🏃‍♂️ Usage
Start the Server
Bash

python run.py
You will see: INFO: Uvicorn running on http://127.0.0.1:8000

Access Documentation
Open your browser to: http://127.0.0.1:8000/docs This provides an interactive Swagger UI to test the API directly.

Run the Test Client
To generate an image and save it to your disk, keep the server running and open a new terminal:

Bash

python test_client.py
Results will be saved in the example_outputs/ folder.

🐳 Docker Instructions
Build and run the application in a container.

Bash

# 1. Build the image
docker build -t text-image-pipeline .

# 2. Run the container
docker run -p 8000:8000 text-image-pipeline
🔌 API Endpoints
1. POST /generate
Generates an image from a text prompt.

Input: {"prompt": "a cyberpunk city"}

Output: Base64 image, CLIP concepts, SAM2 polygons.

2. POST /analyze
Analyzes an existing uploaded image.

Input: {"image": "base64_string..."}

Output: CLIP concepts, SAM2 polygons.

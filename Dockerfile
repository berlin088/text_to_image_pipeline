FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (Git is required for SAM2)
RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install PyTorch CPU (Change to cu118 if using GPU)
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/facebookresearch/segment-anything-2.git

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Start command
CMD ["python", "run.py"]
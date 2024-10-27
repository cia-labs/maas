# MaaS - Model as a Service

## About

This FastAPI-based application is designed to detect elephants in uploaded images using a pretrained YOLO model on the Open Images V7 dataset. It provides an API endpoint for users to upload images and returns a binary response: 1 for the presence or 0 for the absence of an elephant in the image.

## Getting Started

1. Clone the repository:\
   Change the directory to **elephant-detection**

2. Download the YOLO detection model:
   ```
   wget https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x-oiv7.pt
   ```

3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```
   You can specify a custom port using the `--port` option.

## Deploying MaaS as a Docker Container

To deploy the service as a container, follow these steps:

### Create a Dockerfile

Create a file named `Dockerfile` in the root directory of your project with the following content:

```dockerfile
# Use the specified base image
FROM python:3.9.19-slim-bookworm

# Set the working directory
WORKDIR /server

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*


# Copy the main.py file to the working directory
COPY ./main.py .

# Copy the requirements.txt file to the working directory
COPY ./requirements.txt .

# Install Python dependencies
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r ./requirements.txt
# Download the YOLO model
RUN wget https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x-oiv7.pt
EXPOSE 9090

# Set the command to run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9090", "--reload"]
```

### Build and Deploy the Docker Container

1. Build the Docker image:
   ```
   docker build -t maas .
   ```

2. Run the Docker container:
   ```
   docker run -p 9090:9090 maas
   ```

You can now access the Swagger UI at `http://<host-ip>:9090/docs`.

Note: To change the exposed port, modify the `EXPOSE` directive and the `--port` option in the `CMD` line of the Dockerfile.
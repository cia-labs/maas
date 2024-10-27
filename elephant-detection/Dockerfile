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
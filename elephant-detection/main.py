from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
from io import BytesIO

model = YOLO('./yolov8x-oiv7.pt')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        results = model(image)
        
        # Check if any detected object is an elephant
        for result in results:
            for cls, conf in zip(result.boxes.cls, result.boxes.conf):
                class_name = result.names[int(cls)]
                if class_name.lower() == 'elephant':
                    return 1
        
        return 0
    
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": f"Error processing image: {str(e)}"})
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
from io import BytesIO

model = YOLO('./runs/detect/train/weights/best.pt')

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
        temp_results = model(image)
        #print(temp_results)
        if temp_results[0].boxes.shape[0] != 0:
           return 1  
        else:
            return 0
        # Process temp_results as needed
        #return {"predictions": temp_results}
    except Exception as e:
            raise HTTPException(status_code=500, detail={"error": f"Error processing image: {str(e)}"})

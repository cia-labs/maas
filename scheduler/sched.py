import datetime as dt
import os
import time
import base64
import httpx
from scheduler import Scheduler
from dotenv import load_dotenv
from fastapi import FastAPI
from pymongo import MongoClient

load_dotenv()

app = FastAPI()
schedule = Scheduler()

DB_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(DB_URI)
db = client[DB_NAME]
collection = db['feedback']

async def fetch_image_keys():
    return list(collection.find({"qa.0.answer": "No"}, {"imageKey": 1}))


async def fetch_images():
    image_keys = await fetch_image_keys()
    saved_images = []
    image_directory = "/home/ash/Documents/vision-tech/test"
    os.makedirs(image_directory, exist_ok=True)

    async with httpx.AsyncClient() as client:
        for item in image_keys:
            image_key = item.get("imageKey")
            if image_key:
                try:

                    url = f"https://storage.cialabs.org/get/{image_key}"
                    response = await client.get(url)
                    
                    if response.status_code == 200:

                        image_data = base64.b64decode(response.text)
                        filename = f"{image_key}.jpg"
                        image_path = os.path.join(image_directory, filename)
                        
                        with open(image_path, "wb") as image_file:
                            image_file.write(image_data)
                            saved_images.append(image_path)
                            print(f"Saved image to: {image_path}")
                    else:
                        print(f"Failed to fetch image for key {image_key}: {response.status_code}")
                except Exception as e:
                    print(f"Error processing image for key {image_key}: {e}")

    return saved_images

@app.get("/fetch-images")
async def fetch_images_endpoint():
    return await fetch_images()

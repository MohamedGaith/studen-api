from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["student"]
collection = db["students"]  # Assuming the collection is called 'students'

# Create FastAPI app
app = FastAPI()

# API endpoint to get all students data
@app.get("/students")
def get_students():
    data = collection.find()
    json_data = dumps(data)
    return JSONResponse(content=json_data)

# Run: uvicorn main:app --reload

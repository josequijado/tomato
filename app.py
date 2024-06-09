from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import uvicorn
import io
import requests
from routes.model_predict import predict_app
from routes.upload import upload_app


app = FastAPI()

app.include_router(predict_app)
app.include_router(upload_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
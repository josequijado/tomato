from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import uvicorn
import io
import requests

app = FastAPI()

# Función para enviar la imagen al modelo y obtener el resultado
def predict_plant_health(image_bytes: bytes) -> str:
    # Aquí deberías enviar la imagen al modelo y obtener el resultado
    # Puedes usar cualquier biblioteca de IA como TensorFlow, PyTorch, etc.
    # Aquí hay un ejemplo simple usando una solicitud HTTP a una API de modelo ficticia
    model_endpoint = "http://localhost:8000/predict"  # Cambia esto por la URL de tu modelo
    files = {"image": ("image.jpg", image_bytes, "image/jpeg")}
    response = requests.post(model_endpoint, files=files)
    if response.status_code == 200:
        result = response.json()
        return result["prediction"]
    else:
        return "Error al procesar la imagen"

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        prediction = predict_plant_health(contents)
        return JSONResponse(content={"prediction": prediction})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)



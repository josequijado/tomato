import requests

def obtener_recomendacion_imagen(ruta_imagen):
    # Define the API endpoint URL
    url = "http://localhost:11434/v1/chat/completions"

    # Prepare the request data as a dictionary
    data = {
        "model": "llava:latest",  # Corrected model name
        "messages": [
            {
                "role": "system",
                "content": "You are a very helpful assistant. Responde en Español."
            },
            {
                "role": "user",
                "content": f"{ruta_imagen} describe la planta de tomate y dame recomendaciónes para su salud"  # Interpolate the variable
            }
        ],
        "options": {
            "num_predict": 10
        }
    }

    # Set the headers indicating JSON content type
    headers = {"Content-Type": "application/json"}

    # Send the POST request with JSON data
    response = requests.post(url, headers=headers, json=data)

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Extract and print the content values from each message
        for choice in response_data.get("choices", []):
            message = choice.get("message", {})
            content = message.get("content", "Contenido no disponible")
            print(content)
    else:
        print(f"Error: {response.status_code}")  # Print error message if request fails

# Ejemplo de uso
ruta_imagen = "/home/victor/ollama/tomate2.jpg"
obtener_recomendacion_imagen(ruta_imagen)

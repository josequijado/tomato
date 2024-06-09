import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Diagnóstico de Plantas de Tomate")

st.write("Toma una foto de la planta de tomate para obtener un diagnóstico.")

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida.', use_column_width=True)

    if st.button("Enviar para Diagnóstico"):
        st.write("Enviando imagen...")
        # Convertir la imagen a un formato que pueda ser enviado
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        buffered.seek(0)
        
        files = {'file': ("uploaded_image.jpg", buffered, "image/jpeg")}
        
        try:
            response = requests.post("http://localhost:8000/predict", files=files)
            if response.status_code == 200:
                result = response.json()
                st.write("Resultado del diagnóstico:")
                st.write(result['prediction'])  # Mostrar solo la predicción
            else:
                st.write("Error al enviar la imagen.")
                st.write(f"Status code: {response.status_code}")
                st.write(response.text)
        except requests.exceptions.RequestException as e:
            st.write("Exception occurred while sending the image")
            st.write(e)

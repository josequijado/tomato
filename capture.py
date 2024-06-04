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
        
        files = {'file': buffered}
        response = requests.post("api.py", files=files)
        
        if response.status_code == 200:
            result = response.json()
            st.write("Resultado del diagnóstico:")
            st.json(result)
        else:
            st.write("Error al enviar la imagen.")

# Proyecto Tomato

### Identificación de enfermedades en plantas tomateras con visión por computador en un dron

Este proyecto utiliza una webapp para tomar fotos de plantas tomateras con un dron. Las imágenes capturadas son enviadas a una API de FastAPI que las procesa mediante un modelo de machine learning para identificar posibles enfermedades o determinar si la planta está sana. El proyecto es open source y está diseñado para facilitar la detección temprana de enfermedades en cultivos de tomates.

## Estructura del Proyecto

- `api.py`: API de FastAPI que conecta con el modelo para procesar las imágenes.
- `best_model.weights.h5`: Archivo de pesos del modelo entrenado.
- `capture.py`: Script principal para capturar imágenes con el dron.
- `modeloTomates_version2.ipynb`: Notebook de Jupyter con el modelo de detección de enfermedades.

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tomato.git
    cd tomato
    ```

2. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

3. Configurar Git LFS para manejar archivos grandes:
    ```sh
    git lfs install
    git lfs pull
    ```

## Uso

1. Ejecutar la API:
    ```sh
    uvicorn api:app --reload
    ```

2. Capturar una imagen con el dron:
    ```sh
    python capture.py
    ```

3. La imagen será enviada automáticamente a la API y el resultado de la detección se mostrará en la webapp.

## Beneficios del Proyecto

- **Detección temprana de enfermedades**: Ayuda a identificar problemas antes de que se propaguen.
- **Optimización del tiempo**: Uso de drones para cubrir grandes áreas de cultivo rápidamente.
- **Facilidad de uso**: Webapp intuitiva para usuarios sin experiencia técnica.
- **Open Source**: Disponible para la comunidad, fomentando la colaboración y mejora continua.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un fork del proyecto y envía un pull request con tus mejoras.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio o contacta a [tu correo electrónico].

---

Este proyecto se conecta con un Large Language Model (LLM) de llama.cpp y utiliza tecnologías modernas de frontend y backend para proporcionar una solución robusta y eficiente en la detección de enfermedades en plantas tomateras.


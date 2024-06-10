# AI TOMATE
#### *AI TOMATE* es un proyecto de identificación de enfermedades en plantas tomateras mediante el apoyo de la Inteligencia Artificial.


<img src="tomate.png" alt="Tomate">



## ÍNDICE
- [Introducción](#introducción)
- [Acerca del proyecto](#acerca-del-proyecto)
- [Tecnologías empleadas](#tecnologías-empleadas)
- [El futuro del proyecto](#el-futuro-del-proyecto)
- [Conclusión](#conclusión)

## INTRODUCCIÓN

En la agricultura moderna, la identificación temprana y precisa de enfermedades en las plantas es crucial para maximizar el rendimiento de los cultivos y minimizar las pérdidas económicas. Las plantas de tomate, en particular, son susceptibles a una variedad de enfermedades que pueden afectar severamente su crecimiento y productividad. Este proyecto tiene como objetivo desarrollar un sistema basado en inteligencia artificial (IA) capaz de identificar el estado de salud de las plantas de tomate a partir de fotografías y diagnosticar las enfermedades presentes.

Utilizando técnicas avanzadas de aprendizaje automático y visión por computadora desde un dron, hemos entrenado un modelo que analiza imágenes de plantas de tomate para determinar si están sanas o enfermas. En los casos en que se detectan enfermedades, el sistema es capaz de identificar específicamente qué enfermedad afecta a la planta, proporcionando una herramienta valiosa para los agricultores y agrónomos. Este enfoque no solo facilita un diagnóstico más rápido y preciso, sino que también ayuda en la toma de decisiones informadas para el manejo y tratamiento de los cultivos.

El sistema que hemos desarrollado puede, además, ser empleado para otras variedades de cultivos (maiz, patatas, etc) con solo cambios en los datasets empleados para entrenamiento y mínimos ajustes.

## ACERCA DEL PROYECTO
Para llevar a cabo este proyecto de identificación de enfermedades en plantas de tomate, hemos utilizado un conjunto de tecnologías avanzadas, todas centradas en el uso de Python, un lenguaje de programación muy versátil y popular en la comunidad científica y de desarrolladores. Python nos ha permitido manejar grandes volúmenes de datos y aplicar algoritmos complejos de manera eficiente, lo que es fundamental para el análisis de imágenes y la inteligencia artificial.

En el corazón de nuestro sistema se encuentra un modelo de aprendizaje automático (IA), específicamente diseñado para procesar y analizar imágenes. Este modelo ha sido entrenado con miles de fotografías de plantas de tomate, tanto sanas como enfermas, utilizando una tecnología conocida como redes neuronales convolucionales (CNN). Las CNN son especialmente efectivas para el reconocimiento de patrones en imágenes, lo que las hace ideales para este tipo de aplicaciones. Este proceso de entrenamiento permite que el modelo aprenda a distinguir entre las diferentes condiciones de las plantas y las características visuales de varias enfermedades.

Además, hemos empleado bibliotecas y frameworks de Python como TensorFlow y Keras. Estas herramientas proporcionan una plataforma robusta y flexible para construir y entrenar nuestros modelos de IA. TensorFlow y Keras son ampliamente utilizados en el campo de la inteligencia artificial debido a su capacidad para manejar grandes cantidades de datos y realizar cálculos complejos de manera rápida y eficiente.

El uso de estas tecnologías no solo nos ha permitido crear un sistema preciso y fiable, sino que también facilita su implementación en diversas plataformas. Por ejemplo, el modelo puede integrarse en aplicaciones móviles o sistemas de monitoreo en tiempo real, lo que ofrece a los agricultores una herramienta poderosa para el diagnóstico rápido de enfermedades en sus cultivos. De este modo, pueden tomar medidas preventivas o correctivas de manera oportuna, mejorando la salud y productividad de sus plantas de tomate.

## TECNOLOGÍAS EMPLEADAS
Para el desarrollo de nuestro sistema de identificación de enfermedades en plantas de tomate, hemos recurrido a una serie de tecnologías y librerías avanzadas que nos han permitido construir un modelo robusto y eficiente. La elección de estas herramientas ha sido fundamental para garantizar tanto la precisión del diagnóstico como la facilidad de implementación en diferentes entornos. A continuación, presentamos una lista detallada de las principales tecnologías y librerías que han sido empleadas en este proyecto, destacando su importancia y las ventajas que aportan a nuestro sistema.

- **Streamlit**. Es un framework para el diseño de un frontend minimalista, ligero y de alto rendimiento.
- **FastAPI**. Es un framework web moderno y de alto rendimiento para construir APIs con Python, basado en las especificaciones de OpenAPI y JSON Schema.
- **Uvicorn**. Es un servidor ASGI ultrarrápido para Python, diseñado para ejecutar aplicaciones asincrónicas.
- **PIL**. Python Imaging Library es una biblioteca de Python que ofrece potentes capacidades de procesamiento de imágenes.
- **Tensorflow**. Es una biblioteca de código abierto de Google para el aprendizaje automático y la inteligencia artificial, especializada en el entrenamiento y la inferencia de redes neuronales profundas.
- **Numpy**. Es una biblioteca de Python que proporciona soporte para arreglos y matrices multidimensionales, junto con una colección de funciones matemáticas de alto rendimiento para operar con ellas.

Además se ha recurrido a otras librerías y modulos nativos de Python qur complementan el funcionamiento de todo el sistema.

## EL FUTURO DEL PROYECTO
En fases futuras de este proyecto se espera implementar mejoras y ampliaciones de las funcionalidades que incluye. Las próximas actuaciones previstas contemplan lo siguiente:
- **Expansión**. Se expandirá la operativa del sistema a otras variedades de cultivos.
- **Bases de Datos**. Uso de BBDD para almacenar los resultados anualizados, para efectuar comparativas.
- **Implementación de gráficos**. Se implementarán las librerías Matplotlib y Seaborn para graficar los resultados de las visualizaciones y análisis.

## CONCLUSIÓN
El desarrollo de un sistema basado en inteligencia artificial para la identificación de enfermedades en plantas de tomate representa un avance significativo en la agricultura moderna. Este proyecto no solo ofrece una solución precisa y eficiente para el diagnóstico temprano de enfermedades, sino que también proporciona una herramienta valiosa que puede ser adaptada y expandida a otros cultivos, mejorando así la productividad y la sostenibilidad agrícola. La combinación de tecnologías avanzadas y un enfoque centrado en el usuario final garantiza que los agricultores puedan tomar decisiones informadas y oportunas para el manejo de sus cultivos.

A medida que el proyecto avanza, las futuras mejoras y expansiones previstas asegurarán que el sistema continúe evolucionando y adaptándose a las necesidades cambiantes del sector agrícola. La implementación de bases de datos para almacenamiento de resultados y el uso de herramientas de visualización avanzadas como Matplotlib y Seaborn, potenciarán aún más la capacidad de los agricultores para analizar y comprender los datos generados. Con estas innovaciones, estamos posicionados para ofrecer una solución integral y escalable que apoye la agricultura de precisión y contribuya al desarrollo sostenible del sector.

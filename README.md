
# Data-Science---EPPTALLER


🦺 SISTEMA DE DETECCIÓN DE EPP
Monitoreo de seguridad industrial con visión por computador








🧠 Descripción del proyecto

El Sistema de Detección de Equipos de Protección Personal (EPP) es una solución basada en inteligencia artificial que utiliza visión por computador para identificar el uso de elementos de seguridad en entornos industriales.

El sistema detecta automáticamente:

🪖 Casco de seguridad (helmet)
🦺 Chaleco reflectivo (vest)
👷 Persona (person)

El objetivo es mejorar el control de seguridad laboral y reducir riesgos en el entorno de trabajo.

🚀 Problema que resuelve

En entornos industriales es común la falta de cumplimiento de normas de seguridad, lo cual puede generar:

Accidentes laborales ⚠️
Sanciones legales 📉
Riesgos operativos 🏭

La supervisión manual es limitada, por lo que este sistema automatiza el monitoreo de seguridad mediante IA.

🧠 Modelo de Inteligencia Artificial

El sistema está basado en:

YOLOv8
📊 Entrenamiento del modelo
Dataset: +2000 imágenes etiquetadas de EPP
Clases:
helmet
vest
person
Framework: Ultralytics YOLO
Modelo final: best.pt
🏗️ Arquitectura del sistema
Usuario sube imagen
        ↓
Interfaz Streamlit
        ↓
Modelo YOLOv8
        ↓
Detección de objetos
        ↓
Resultados visuales + alertas de seguridad


💻 Tecnologías utilizadas
Python
Streamlit
PyTorch
OpenCV
Ultralytics YOLO
Pandas
Pillow


📁 Estructura del proyecto
ppe-detection/
│
├── notebook/              # Entrenamiento del modelo
├── app.py                 # Aplicación web (Streamlit)
├── best.pt                # Modelo entrenado
├── requirements.txt       # Dependencias
├── runtime.txt            # Versión de Python
├── video/                 # Demo del sistema
├── logo.jpg              # Identidad visual
└── README.md
⚙️ Instalación y ejecución

1️⃣ Clonar repositorio
git clone https://github.com/Balox2991/Data-Science---EPPTALLER.git
cd Data-Science---EPPTALLER

2️⃣ Crear entorno virtual
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Ejecutar aplicación
streamlit run app.py


🖥️ Funcionalidades
📤 Carga de imágenes
🧠 Detección automática de EPP
📦 Visualización con bounding boxes
⚠️ Alertas de incumplimiento de seguridad
📊 Resultados de detección en tiempo real
📊 Resultados del sistema

El modelo identifica:

Elemento	Estado
Casco	✔ / ✖
Chaleco	✔ / ✖
Persona	✔
⚠️ Limitaciones
Depende de la calidad del dataset
Puede fallar en condiciones de poca iluminación
Requiere reentrenamiento para nuevos tipos de EPP
No está optimizado aún para cámaras en tiempo real
🔮 Mejoras futuras
🎥 Integración con cámaras en vivo (CCTV)
📡 Implementación en tiempo real
📊 Panel de análisis de seguridad
🔔 Sistema de alertas automáticas
🧠 Optimización del modelo con datasets industriales reales

Aplicación en línea 
👉 [https://tu-app-streamlit.streamlit.app](https://data-science---epptaller-kkcb8khugxnkd4vyuio65k.streamlit.app](https://data-science---epptaller-kkcb8khugxnkd4vyuio65k.streamlit.app/)/


👨‍💻 Autor

Proyecto desarrollado como prototipo académico de:

Visión por computador aplicada a seguridad industrial

Juan David Amaya Quintero





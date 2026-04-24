import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

# Config
st.set_page_config(page_title="Detector EPP", layout="centered")

st.title("🦺 Detector de Equipos de Protección Personal")
st.write("Detecta casco, chaleco, guantes y personas en imágenes.")

# Sidebar (control)
st.sidebar.header("⚙️ Configuración")
conf_threshold = st.sidebar.slider("Confianza mínima", 0.0, 1.0, 0.5)

# Verificar modelo
if not os.path.exists("best.pt"):
    st.error("❌ No se encontró el modelo best.pt")
    st.stop()

# Cargar modelo
model = YOLO("best.pt")

# Subir imagen
uploaded_file = st.file_uploader("📂 Sube una imagen", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🖼️ Imagen original", use_column_width=True)

    img_array = np.array(image)

    # Predicción
    results = model(img_array)

    # Filtrar resultados por confianza
    filtered_boxes = []
    for r in results:
        for box in r.boxes:
            if float(box.conf) >= conf_threshold:
                filtered_boxes.append(box)

    # Mostrar imagen anotada
    annotated = results[0].plot()
    st.image(annotated, caption="🔍 Detección", use_column_width=True)

    # Mostrar resultados
    st.subheader("📊 Resultados:")

    if len(filtered_boxes) == 0:
        st.warning("No se detectaron objetos con esa confianza")
    else:
        for box in filtered_boxes:
            clase = model.names[int(box.cls)]
            confianza = float(box.conf)
            st.write(f"• {clase} ({confianza:.2f})")

    st.success("✅ Proceso completado")
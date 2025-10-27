import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import json

# -------------------- Load Model and Class Mapping --------------------
model = tf.keras.models.load_model("parkinson_model.h5")

# Load class names (0 -> healthy, 1 -> parkinson)
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)
class_indices = {int(k): v for k, v in class_indices.items()}

# -------------------- Helper Function --------------------
def load_and_preprocess_image(image, target_size=(224, 224)):
    img = image.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype("float32") / 255.0
    return img_array

# -------------------- Streamlit UI --------------------
st.title("🧠 Parkinson’s Disease Prediction using Handwriting")
st.write("Upload a spiral or wave handwriting image to check for Parkinson’s patterns.")

uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Predict"):
        preprocessed_img = load_and_preprocess_image(image)
        predictions = model.predict(preprocessed_img)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        predicted_class_name = class_indices[predicted_class_index]

        st.subheader(f"🩺 Predicted Class: **{predicted_class_name.upper()}**")
        st.write("Confidence:", f"{np.max(predictions) * 100:.2f}%")


import streamlit as st
import numpy as np
from PIL import Image
from utils import create_pencil_sketch

st.title("Pencil Sketch Transformer")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Display original image
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    # PRocess the image to create a pencil sketch
    pencil_sketch = create_pencil_sketch(image_np)

    # Display pencil sketch
    st.subheader("Pencil sketch")
    st.image(pencil_sketch, use_container_width=True, clamp=True, channels="GRAY")
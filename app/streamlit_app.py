import streamlit as st
import requests
from io import BytesIO
import random

API_URL = "http://localhost:8001/predict"

st.set_page_config(page_title="Real vs Fake (stub)")
st.title("Real vs Fake — Stub Demo")

file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])
if file:
    st.image(file, caption="Uploaded", use_container_width=True)

if st.button("Get score"):
    if not file:
        st.warning("Please upload an image first.")
    else:
        try:
            bytes_data = file.read()
            files = {"file": ("upload.png", BytesIO(bytes_data), "image/png")}
            r = requests.post(API_URL, files=files, timeout=5)
            r.raise_for_status()
            data = r.json()
            st.success(f"Score: {data['score']:.2f} → {data['label']} (model: {data['model_version']})")
        except Exception:
            # fallback: offline random score so the UI still proves wiring
            score = round(random.random(), 2)
            label = "fake" if score >= 0.5 else "real"
            st.info(f"(Fallback) Score: {score:.2f} → {label} (model: stub-offline)")

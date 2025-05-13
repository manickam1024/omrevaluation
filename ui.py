import streamlit as st
import os
import shutil
import subprocess

UPLOAD_DIR = "samples/inputs"
OUTPUT_DIR = "outputs"

st.title("OMR Sheet Evaluation")

uploaded_file = st.file_uploader("Upload OMR Sheet", type=["jpg", "png", "pdf"])

if uploaded_file:
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name}")

    if st.button("Run Evaluation"):
        st.info("Processing...")
        result = subprocess.run(
            ["python", "main.py", "--outputDir", OUTPUT_DIR],
            capture_output=True, text=True
        )
        st.text(result.stdout)
        st.text(result.stderr)
        st.success("Evaluation completed. Check the outputs folder.")

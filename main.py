import streamlit as st
from PIL import Image
import albumentations as A
import cv2
import numpy as np
sidebar_title = st.sidebar.title("Preprocessing")

st.header("Result")
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])

options = st.multiselect('methods', ['CLAHE', 'threshold', 'sobel'])

st.sidebar.write('You selected:', options)
transformed_list = []

if img_file:
    col_ori, col_res = st.beta_columns(2)
    img = Image.open(img_file)
    image = np.asarray(img)
    for op in options:
        if op == "CLAHE":
            transformed_list.append(A.CLAHE(p=1))
        if op == "threshold":
            transform = A.Compose(transformed_list)
            transformed = transform(image=image)
            transformed_image = transformed["image"]
            cv2.threshold(transformed_image, 128, 255)
            res = Image.fromarray(transformed_image)

    transform = A.Compose(transformed_list)
    transformed = transform(image=image)
    transformed_image = transformed["image"]
    res = Image.fromarray(transformed_image)
    with col_ori:
        st.image(img, use_column_width=True)
    with col_res:
        st.image(res, use_column_width=True)








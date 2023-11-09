#!/bin/env/python

from flask import Flask, request
from imageprocessor import ImageProcessor

app = Flask(__name__)


@app.route("/ocr/image/frombytes", methods=["POST"])
def get_image_text():
    image = request.files["image"]
    img_bytes = image.read()
    if not img_bytes:
        return {"Error": "Sube bien la imagen perro"}, 400
    
    processor = ImageProcessor()
    text = processor\
    .load_from_bytes(img_bytes)\
    .greyscale()\
    .ocr()

    return {"text":f"{text}"}, 200
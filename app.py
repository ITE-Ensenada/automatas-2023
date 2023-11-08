#!/bin/env/python

from flask import Flask, request
from imageprocessor import ImageProcessor

app = Flask(__name__)


@app.route("/ocr/image/frombase64", methods=["POST"])
def get_image_text():
    image_str = request.args.get("image")
    if not image_str:
        return {"Error": "Sube bien la imagen perro"}, 200
    
    processor = ImageProcessor()
    text = processor\
    .load_from_string(image_str)\
    .greyscale()\
    .ocr()

    return {"text":f"{text}"}, 200
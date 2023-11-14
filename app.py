#!/bin/env/python

import os
from flask import Flask, request
from imageprocessor import ImageProcessor

app = Flask(__name__)


@app.route("/ocr/image/frombytes", methods=["POST"])
def get_image_text():
    image = request.files["image"]
    img_bytes = image.read()
    if not img_bytes:
        return {"Error": "Provide a valid image."}, 400

    processor = ImageProcessor()
    text = processor.load_from_bytes(img_bytes).greyscale().ocr()

    return {"text": f"{text}"}, 200


@app.route("/ocr/pdf/frombytes", methods=["POST"])
def get_pdf_text():
    pdf = request.files["pdf"]
    pdf.save("temp.pdf")
    if not pdf:
        return {"Error": "Provide a valid PDF file."}, 400

    processor = ImageProcessor()
    text = processor.load_from_pdf("temp.pdf").greyscale().ocr()
    os.remove("temp.pdf")

    return {"text": f"{text}"}, 200

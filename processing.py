import cv2
from PIL import ImageFilter, Image, ImageEnhance
from cv2 import dnn_superres


def blur_image(img_path: str):
    Image.open(img_path).filter(ImageFilter.BLUR).save(img_path)


def contour(img_path: str):
    Image.open(img_path).filter(ImageFilter.CONTOUR).save(img_path)


def enhance_color(img_path: str):
    img = Image.open(img_path)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(1.5)
    img2.save(img_path)

def greyscale(img_path: str):
    img = Image.open(img_path)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(0)
    img2.save(img_path)


def upscale_image(img_path: str):
    sr = dnn_superres.DnnSuperResImpl_create()
    image = cv2.imread(img_path)
    path = "EDSR_x4.pb"
    sr.readModel(path)
    sr.setModel("edsr", 4)
    result = sr.upsample(image)
    cv2.imwrite("./upscaled.png", result)



import cv2
import numpy as np
import pytesseract
from typing_extensions import Self
from PIL import ImageFilter, Image, ImageEnhance
from cv2 import dnn_superres
from pdf2image import convert_from_path
from io import BytesIO
from cv2.typing import MatLike


class ImageProcessor:
    def __init__(self):
        self.image: Image.Image
        self.ocv_image: MatLike

    def load_from_bytes(self, b: bytes) -> Self:
        """
        Load an image from a bytes object.

        This method takes a bytes object containing image data, opens it as an image,
        and converts it to both a PIL Image and an OpenCV image for further processing.

        Args:
            b (bytes): The bytes object containing image data.

        Raises:
            Exception: If an error occurs while opening the image from bytes.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        try:
            self.image = Image.open(BytesIO(b))
            self.ocv_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)

        except:
            raise Exception("Could not open image from bytes.")

        return self

    def load_from_path(self, path: str) -> Self:
        """
        Load an image from a file path.

        Args:
            path (str): The path to the image file.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        try:
            self.image = Image.open(path)
            self.ocv_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)

        except Exception as e:
            print("Could not load image", e)

        return self

    def load_from_pdf(self, path: str) -> Self:
        """
        Load an image from a PDF file, converting the first page to an image.

        This method reads the first page of a PDF file and converts it to an image,
        which can then be processed using other methods of the ImageProcessor class.

        Args:
            path (str): The path to the PDF file.

        Raises:
            Exception: If an error occurs while converting the PDF or if multiple page PDFs are not supported.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """

        try:
            images = convert_from_path(path)

            if len(images) > 1:
                print(
                    "Multiple page PDFs are not supported. Only first page will be saved."
                )

            self.image = images[0]
            self.ocv_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)

        except Exception as e:
            raise Exception("Couldn't convert PDF", e)

        return self

    def save(self, path: str, compression = False) -> None:
        """
        Save the current image to a file.

        Args:
            path (str): The path to save the image to.
        """
        if compression:
            width, height = self.image.size
            self.image = self.image.resize(size=[width/2, height/2])

        self.image.save(path)

    def greyscale(self) -> Self:
        """
        Convert the image to grayscale.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        converter = ImageEnhance.Color(self.image)
        self.image = converter.enhance(0)

        return self

    def contour(self) -> Self:
        """
        Apply a contour filter to the image.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        self.image = self.image.filter(ImageFilter.CONTOUR)

        return self

    def blur_image(self) -> Self:
        """
        Apply a Gaussian blur to the image.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        self.image = self.image.filter(ImageFilter.GaussianBlur)

        return self

    def enhance_color(self, factor: float) -> Self:
        """
        Enhance the color of the image by a specified factor.

        Args:
            factor (float): The enhancement factor (1.0 means no change).

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        converter = ImageEnhance.Color(self.image)
        self.image = converter.enhance(factor=factor)
        return self

    def upscale(self) -> Self:
        """
        Upscale the image using a super-resolution model.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        sr = dnn_superres.DnnSuperResImpl_create()  # pyright: ignore
        model_path = "ESPCN_x2.pb"
        sr.readModel(model_path)
        sr.setModel("espcn", 2)
        self.ocv_image = sr.upsample(self.ocv_image)

        return self

    def ocr(self) -> str:
        """
        Perform Optical Character Recognition (OCR) on the current image and print the detected text.
        """
        return pytesseract.image_to_string(self.image, lang="spa")


if __name__ == "__main__": 
    
    import requests
    
    img_bytes: bytes
    with open("assets/reti.jpg", "rb") as img_file:
        img_bytes = img_file.read()

    text = requests.post(
            "http://localhost:5000/ocr/image/frombytes", 
            files={"image": img_bytes}
        ).text
    print(text)
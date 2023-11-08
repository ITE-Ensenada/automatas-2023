import cv2
import numpy as np
import pytesseract
from PIL import ImageFilter, Image, ImageEnhance
from cv2 import dnn_superres
from pdf2image import convert_from_path, pdfinfo_from_path
from base64 import urlsafe_b64decode as b64decode
from base64 import urlsafe_b64encode
from io import BytesIO


class ImageProcessor:
    def __init__(self):
        self.image: Image.Image = None

    def load_from_path(self, path: str):
        """
        Load an image from a file path.

        Args:
            path (str): The path to the image file.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        try:
            self.image = Image.open(path)
            self.ocv_image = cv2.cvtColor(
                np.array(self.image), cv2.COLOR_RGB2BGR)

        except Exception as e:
            print("Could not load image", e)

        return self

    def load_from_string(self, base64str: str):
        """
        Load an image from a base64-encoded string.

        Args:
            base64str (str): The base64-encoded image data.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        try:
            self.image = Image.open(BytesIO(b64decode(base64str)))
            self.ocv_image = cv2.cvtColor(
                np.array(self.image), cv2.COLOR_RGB2BGR)
        except Exception as e:
            print("Could not load image", e)

        return self

    def load_from_pdf(self, path: str):
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
                print("Multiple page PDFs are not supported. Only first page will be saved.")

            self.image = images[0]
            self.ocv_image = cv2.cvtColor(
                np.array(self.image), cv2.COLOR_RGB2BGR)

        except Exception as e:
            raise ("Couldn't convert PDF", e)

    def save(self, path: str):
        """
        Save the current image to a file.

        Args:
            path (str): The path to save the image to.
        """
        self.image.save(path)

    def greyscale(self):
        """
        Convert the image to grayscale.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        converter = ImageEnhance.Color(self.image)
        self.image = converter.enhance(0)

        return self

    def contour(self):
        """
        Apply a contour filter to the image.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        self.image = self.image.filter(ImageFilter.CONTOUR)

        return self

    def blur_image(self):
        """
        Apply a Gaussian blur to the image.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        self.image = self.image.filter(ImageFilter.GaussianBlur)

        return self

    def enhance_color(self, factor: float):
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

    def upscale(self):
        """
        Upscale the image using a super-resolution model.

        Returns:
            ImageProcessor: The ImageProcessor instance.
        """
        sr = dnn_superres.DnnSuperResImpl_create()
        model_path = "ESPCN_x2.pb"
        sr.readModel(model_path)
        sr.setModel("espcn", 2)
        self.ocv_image = sr.upsample(self.ocv_image)

        return self

    def ocr(self):
        """
        Perform Optical Character Recognition (OCR) on the current image and print the detected text.
        """
        return pytesseract.image_to_string(self.image, lang="spa")


if __name__ == "__main__":
    urlstr = str

    with open("assets/reti.jpg", "rb") as img:
        urlstr = urlsafe_b64encode(img.read())

    processor = ImageProcessor()
    text = processor\
        .load_from_string(urlstr)\
        .greyscale()\
        .ocr()

    print(text)

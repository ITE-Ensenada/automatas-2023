import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
import numpy as np
    # Load the image

def ocr(img_path):
    
    text = pytesseract.image_to_string(img_path,lang='spa')
    print(text)


def rectangles() -> list:

    image = cv2.imread('reti.jpg')
    
    # Blur, then greyscale, then borders, then conts.
    blur = cv2.pyrMeanShiftFiltering(image, 11, 21)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    cnts = cnts[0] if len(cnts) == 2 else cnts[1] #bc findContours returns a tuple
    
    cropped_rectangles = []
    
    for c in cnts:
        peri = cv2.arcLength(c, True) #Perimeter
        approx = cv2.approxPolyDP(c, 0.01 * peri, True) #Actual figure
        
        if len(approx) == 4: # If detected figure has 4 sides
            x, y, w, h = cv2.boundingRect(approx)
            
            # Currently hard-coded to ISC!
            if 100 < w < 150  and 80 < h < 95: # Exclude mini rectangles
                cropped_rectangle = image[y:y+h, x:x+w]
                cropped_rectangles.append(cropped_rectangle)

    return cropped_rectangles


def main() -> None:

    cropped_rectangles = rectangles()
    print(f"Detected {len(cropped_rectangles)} subjects")

    for i,r in enumerate(cropped_rectangles):
        img_path = f"cropped_rectangles/img_{i}.jpg"
        cv2.imwrite(img_path, r)
        ocr(img_path)


if __name__ =="__main__":main()
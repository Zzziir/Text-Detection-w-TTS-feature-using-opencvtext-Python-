import cv2
from PIL import Image
from pytesseract import pytesseract
import sys
import pyttsx3

camera=cv2.VideoCapture(1, cv2.CAP_DSHOW)
object_detector = cv2.createBackgroundSubtractorMOG2()
text_speech = pyttsx3.init()
# bright = 128
# focus = 0
# camera.set(cv2.CAP_PROP_BRIGHTNESS,(bright))
# camera.set(cv2.CAP_PROP_FOCUS, (focus))

while True:
    _,image=camera.read()
    #used to test camera readability
    mask = object_detector.apply(image) 
    cv2.imshow("Mask", mask)
    cv2.imshow('image',image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',image)
        break

    #OPTION KEYS TO INCREASE BRIGHTNESS AND FOCUS
    #ps: gumagana lang sa camera na may ganong feature

    # if  cv2.waitKey(1)& 0xFF==ord('.'):
    #     focus = focus + 5
    #     camera.set(cv2.CAP_PROP_FOCUS, (focus))

    # if  cv2.waitKey(1)& 0xFF==ord(','):
    #     focus = focus - 5
    #     if focus < 0:
    #         focus = 0
    #     camera.set(cv2.CAP_PROP_FOCUS, (focus))

    # if cv2.waitKey(1)& 0xFF==ord('='):
    #         bright = bright + 5
    #         camera.set(cv2.CAP_PROP_BRIGHTNESS, (bright))

    # if cv2.waitKey(1)& 0xFF==ord('-'):
    #     bright = bright - 5
    #     if bright < 0:
    #         bright = 0
    #     camera.set(cv2.CAP_PROP_BRIGHTNESS, (bright))
    
#Function to read the text from the video capture
def tesseract():
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = "test1.jpg"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.open(image_path))
        print(text[:-1])
        text_speech.say(text)
        text_speech.runAndWait()
tesseract()
# Modules
import cv2
from PIL import Image
from IPython.display import display


def showBW(img):
    # Converting BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    display(Image.fromarray(img))


def show(img):
    # Converting BGR to BW.
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    display(Image.fromarray(img))
    
def imshow(img):
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Converting BGR to RGB
    display(Image.fromarray(img))
    
def imshowBW(img):
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting BGR to RGB
    display(Image.fromarray(img))


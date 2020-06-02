from PIL import Image
from pylab import *
import numpy

im = array(Image.open('image.jpg').convert('L'))
gray()
def MakeNegative(im):
    return 255 -im       #negative image
def MakeGrayInInterval(im):
    return (100.0/255) *im + 100 # Clamp to interval 100 ... 200
def MakeGray(im):
    return 255.0 *(im/255.0)**2

Image.fromarray(MakeNegative(im).astype(numpy.uint8)).save('Negative.jpg')
Image.fromarray(MakeGrayInInterval(im).astype(numpy.uint8)).save('GrayInterval.jpg')
Image.fromarray(MakeGray(im).astype(numpy.uint8)).save('Gray.jpg')
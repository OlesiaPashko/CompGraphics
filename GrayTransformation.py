from PIL import Image
from pylab import *

im = array(Image.open('image.jpg').convert('L'))
gray()
im2 = 255 -im       #negative image
im3 = (100.0/255) *im + 100 # Clamp to interval 100 ... 200
im4 = 255.0 *(im/255.0)**2

imshow(im4)

show();
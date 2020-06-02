from scipy.ndimage.filters import maximum_filter
from matplotlib.pyplot import gray
from skimage import img_as_int
from PIL import Image
import numpy
from scipy import ndimage

def getMaximumFilteredImage(image, *, size):
    return (
        maximum_filter(image, size)
    )

def GetGrayscaledImage(path_):
    im = numpy.array(Image.open(path_).convert('L'))
    gray()
    return im

image = GetGrayscaledImage('dog.jpg')
maximum_filtered_image = getMaximumFilteredImage(image, size=5)
Image.fromarray(maximum_filtered_image.astype(numpy.uint8)).save( 'MaximumFilteredDog.jpg')
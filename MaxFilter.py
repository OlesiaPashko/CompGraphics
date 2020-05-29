from scipy.ndimage.filters import maximum_filter
from matplotlib.pyplot import gray
from skimage import img_as_int
from PIL import Image
import numpy
from scipy import ndimage

def get_maximum_filtered_image(image, *, size):
    return (
        maximum_filter(image, size)
    )

def get_grayscaled_image(path_):
    im = numpy.array(Image.open(path_).convert('L'))
    gray()
    return im

image = get_grayscaled_image('dog.jpg')
maximum_filtered_image = get_maximum_filtered_image(image, size=5)
Image.fromarray(maximum_filtered_image.astype(numpy.uint8)).save( 'maximum_filtered_dog.jpg')
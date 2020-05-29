from matplotlib.pyplot import gray
from skimage import img_as_int
from PIL import Image
import numpy
from scipy import ndimage

def get_grayscaled_image(path_):
    im = numpy.array(Image.open(path_).convert('L'))
    gray()
    return im

def _detect_edges_with_operator(image, operator):
    prewitt_vertical = numpy.array(
        operator,
        dtype='float64'
    )
    return ndimage.convolve(
        img_as_int(image), prewitt_vertical)


def detect_edges_with_horizontal_operator(image):
    horizontal_operator = [
        [-1, -1, 1],
        [0, 0, 0],
        [1, 1, 1]
    ]
    return _detect_edges_with_operator(image, horizontal_operator)


image = get_grayscaled_image('dog.jpg')
horizontally_transformed_image = detect_edges_with_horizontal_operator(image)
Image.fromarray(horizontally_transformed_image.astype(numpy.uint8)).save(('horizontally_transformed_dog.jpg'))

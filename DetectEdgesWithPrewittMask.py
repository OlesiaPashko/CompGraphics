from matplotlib.pyplot import gray
from skimage import img_as_int
from PIL import Image
import numpy
from scipy import ndimage

path = 'dog.jpg'
def GrayscalImage():
    im = numpy.array(Image.open(path).convert('L'))
    gray()
    return im


def DetectEdgesWithHorizontalOperator(image):
    horizontal_operator = [
        [-1, -1, 1],
        [0, 0, 0],
        [1, 1, 1]
    ]
    prewitt_vertical = numpy.array(
        horizontal_operator,
        dtype='float64'
    )
    return ndimage.convolve(
        img_as_int(image), prewitt_vertical)


image = GrayscalImage()
horizontally_transformed_image = DetectEdgesWithHorizontalOperator(image)
Image.fromarray(horizontally_transformed_image.astype(numpy.uint8)).save('HorizontallyTransformedDog.jpg')
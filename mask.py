import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters

def load_image(user_upload):

    """a function that loads the image the user has uploaded to flask"""

    image = skimage.io.imread(user_upload)
    return image


def grey_image(image):

    """converts the image to grayscale"""

    gray_image = skimage.color.rgb2gray(image)
    return gray_image


def blur_image(gray_image):

    """"blurs the image to denoise"""

    blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
    return blurred_image


def find_threshold(blurred_image):

    """"finds values of to turn pixels above that value 'off'"""

    t= skimage.filters.threshold_otsu(blurred_image)
    return t


def create_mask(t, blurred_image):

    """create a binary mask with the threshold found by the find
    threshold function"""

    binary_mask = blurred_image > t
    return binary_mask


def save_mask(binary_mask):

    """saves mask created by the create_mask function to the statuc/mask
    directory"""

    plt.imsave("static/masks/mask.jpg", binary_mask, cmap='gray')

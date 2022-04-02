import numpy as np
from PIL import Image

def predict_image(generator,mask):
    mask=np.array(mask)/255
    mask[mask>0.5]=1
    mask[mask<=0.5]=0
    img = mask.reshape((1,256,256,3))
    img_final = generator(img,training=True)[0]
    return np.array(img_final)


def preproc(file_name):

    """takes an image loads it with PIL, resises to RGB"""

    img = Image.open(file_name)
    img = img.convert('RGB')
    img = img.resize((256,256))
    return img

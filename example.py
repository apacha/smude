from skimage.io import imread, imsave
from smude import Smude

image = imread('images/input_fullsize.jpg')
smude = Smude(use_gpu=False)
result = smude.process(image)
imsave('result.png', result)

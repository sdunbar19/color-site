from PIL import Image as Img
import numpy as np
import colorsys

def process(image_path):
    img = Img.open(image_path)
    img2 = img.convert('HSV')
    hsv_array = np.asarray(img2) # values between 0 and 255
    pixel_zero = hsv_array[0][0]
    rgb = colorsys.hsv_to_rgb(pixel_zero[0]/float(255), pixel_zero[1]/float(255), pixel_zero[2]/float(255))
    hexa = '#%02x%02x%02x' % (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
    return {'data': hexa}
__author__ = 'johnfulgoni'
from PIL import Image, ImageFilter, ImageDraw
import image_slicer
import numpy
import datetime

def process_image(im, slices):
   tiles = image_slicer.slice(im, slices, save=False)
   for tile in tiles:
       square = tile.image.load()
       replace_pixels(tile.image, square)
   return image_slicer.join(tiles)

def replace_pixels(img, square):
    pixel_list = []
    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            pixel_list.append(square[i, j])

    avg_pixel = tuple(numpy.mean(tuple(pixel_list), axis=0))
    pixel_val = (int(avg_pixel[0]), int(avg_pixel[1]), int(avg_pixel[2]))
    print avg_pixel, pixel_val
    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            square[i, j] = pixel_val

if __name__ == '__main__':
    filepath = '/Users/johnfulgoni/PycharmProjects/python-projects/TwistedFantasy/images/alec_monopoly.jpg'
    twisted_image = process_image(filepath, 200)
    # twisted_image.show()
    current_time = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')
    twisted_image.save('/Users/johnfulgoni/PycharmProjects/python-projects/TwistedFantasy/results/' + current_time + '.png')
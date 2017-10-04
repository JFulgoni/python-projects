__author__ = 'johnfulgoni'
from PIL import Image, ImageFilter, ImageDraw
import image_slicer
import numpy
import datetime
import sys

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
    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            square[i, j] = pixel_val

# TODO in the future I want to add optional arguments
# Add arguments to show/hide result, choose save location
def process_arguments():
    if len(sys.argv) is 3:
        filepath = sys.argv[1]
        slices = float(sys.argv[2])
    else:
        print 'Argument conditions not satisfied, using default args.'
        filepath = '/Users/johnfulgoni/PycharmProjects/python-projects/TwistedFantasy/images/alec_monopoly.jpg'
        slices = 200
    return filepath, slices

if __name__ == '__main__':
    filepath, slices = process_arguments()

    twisted_image = process_image(filepath, slices)
    # twisted_image.show()
    current_time = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')
    twisted_image.save('/Users/johnfulgoni/PycharmProjects/python-projects/TwistedFantasy/results/' + current_time + '.png')
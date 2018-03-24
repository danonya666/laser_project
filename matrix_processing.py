from splitting_frames import *
from PIL import Image

"""def find_laser(width, height, pix):
    for i in range(height):
        counter = 0
        for j in range(width):
            rgb = pix[j, i]
            if (rgb[0] > 80):
                counter += 1
            else:
                if (counter > width // 3)   #if it's more than a third of pixels wide --> YSPEH! Laser found!
                    laser_matrix =  #let's create a laser matrix here
                counter = 0

    return laser_matrix"""


this_image = Image.open('check.png')
im_columns = this_image.width
im_rows = this_image.height

this_pix = this_image.load()    #remember, [columns, rows]




from config import *
from PIL import Image

#def for checking if a pixel is LASER
def is_laser(pix):
    if(pix > 80):
        return 1
    else:
        return 0



def find_laser(width, height, pix):
    #laser_matrix = [[]] # matrix where the laser pixels lie
    r_counter = 0 #row counter counts the current row of our laser matrix
    c_counter = 0 #column counter for the current column of our laser matrix
    counter = [] # counter of red pixels in a line
    row_has_laser = [] # true if a row has a red pixel

    # initializing the arrays
    for i in range(height):
        counter.append(0)
        row_has_laser.append(0)

        #countring red dots in lines
    for i in range(height):
        for j in range(width):
            #print(i, j)
            r = pix[j, i][0] # red component of the pixel
            g = pix[j, i][1] # green component of the pixel
            b = pix[j, i][2] # blue component of the pixel
            row_has_laser = 0  # int for finding out if the row has a laser pixel
            if (is_laser(r)): # if pixel is red enough
                #row_has_laser[0] = 1
                counter[i] += 1

    return counter

"""
            else:
                if (counter > width // 3):   #if it's more than a third of pixels wide --> YSPEH! Laser found!
                    return laser_matrix #Our laser is found, let's return it!
                else:
                    laser_matrix = [[]] #if counter is too small and the red part has ended, that means that this is just a glare, not a matrix
                                        #so we delete our laser_matrix and start looking for the REAL LASER
                    counter = 0         #Also zeroing some vars


"""



this_image = Image.open('check.png')
im_columns = this_image.width #Detect width
im_rows = this_image.height #Detect height

"""
im_columns = the number of columns in a picture
im_rows = the number of rows in a picture
"""

this_pix = this_image.load()    #remember, [columns, rows]

"""
this_pix[j, i][k] - pixel with 
width = i 
height = j
color attribute = k
"""

#printing our picture by pixels to output.txt
#just to check if everything is alright
for i in range(im_rows):
    f.write('\n')
    f.write('\n')
    f.write(str(i) +  " - " + str(find_laser(im_columns, im_rows, this_pix)[i]))
    for j in range(im_columns):
        #f.write('[' + str(this_pix[j, i][0]) + " " + str(this_pix[j, i][1]) + " " + str(this_pix[j, i][2]) + ']') #Every pixel is [R, G, B]
        #f.write(str(i) + "-" + str(j) + " ") #For checking the indexation
        pass



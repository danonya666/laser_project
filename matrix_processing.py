from config import *
from PIL import Image

#def for checking if a pixel is LASER
def is_laser(pix):
    if(pix > 80):
        return 1
    else:
        return 0

# should be used like find_laser(im_columns, im_rows, this_pix)
# returns a list with the number of red pixels in every row
def find_laser(width, height, pix):
    r_counter = 0 #row counter counts the current row of our laser matrix
    c_counter = 0 #column counter for the current column of our laser matrix
    counter = [] # counter of red pixels in a line
    row_has_laser = [] # true if a row has a red pixel

    # initializing the lists
    for i in range(height):
        counter.append(0)

        #countring red dots in lines
    for i in range(height):
        for j in range(width):
            #print(i, j)
            r = pix[j, i][0] # red component of the pixel
            g = pix[j, i][1] # green component of the pixel
            b = pix[j, i][2] # blue component of the pixel
            row_has_laser = 0  # int for finding out if the row has a laser pixel
            if (is_laser(r)): # if pixel is red enough
                counter[i] += 1

    return counter

# function for returning the place of the laser
def find_laser_matrix_place(counter, height):
    num = 0 # Here we gonna store the position of laser
    square = [] # list of squares of suspicions to laser
    i = 0
    while(i < height):
        if(counter[i] > 0):  # if a line has red dots
            square.append([0, num]) # initializing a place in square list for this object
            while(counter[i] > 0):
                square[num][0] += counter[i] # counting the square of the object
                i += 1
            num += 1 # going to the next item in square list
        i += 1
    square.sort(reverse = True) # sorting squares, biggest square is in [0]
    return square[0][1] # returning the place of the laser

# function for returning the medium intensity of the laser
# SHOULD BE RENAMED
# position - result of the function find_laser_matrix_place
# counter - result of the function find_laser
def get_laser_matrix(pix, position, width, height, counter):
    num = 0
    i = 0 # putting i counter to the place of the laser
    while(num != position or counter[i] == 0):
        if(counter[i] > 0):
            i += 1

            while(counter[i] != 0):
                i += 1
            num += 1
        i += 1

    red_sum = 0 # sum of the red component in a laser
    pixel_counter = 0 # quantity of pixels in a laser
    intensity = 0 # = red_sum / pixel_counter
    j = 0
    while(counter[i] != 0): # while we are in the laser
        while(j < width): # while we are in the row
            while(not is_laser(pix[j, i][0]) and j < width - 1):
                j += 1 # this skips the black dots in a row
            red_sum += pix[j, i][0]
            pixel_counter += 1
            j += 1
        i += 1
        j = 0
    intensity = red_sum / pixel_counter
    return intensity


this_image = Image.open('check.png')
im_columns = this_image.width #Detect width
im_rows = this_image.height #Detect height

"""
im_columns = the number of columns in a picture
im_rows = the number of rows in a picture
"""

this_pix = this_image.load()    #remember, [columns, rows]

counter = find_laser(im_columns, im_rows, this_pix) # the list with the numbers of red dots in each row
position = find_laser_matrix_place(counter, im_rows) # the place of the matrix
print(get_laser_matrix(this_pix, position, im_columns, im_rows, counter)) # printing the intensity

"""
#Just some printing into a file
for i in range(im_rows):
    f.write('\n')
    f.write('\n')
    #f.write(str(i) +  " - " + str(find_laser(im_columns, im_rows, this_pix)[i]))
    for j in range(im_columns):
        #f.write('[' + str(this_pix[j, i][0]) + " " + str(this_pix[j, i][1]) + " " + str(this_pix[j, i][2]) + ']') #Every pixel is [R, G, B]
        #f.write(str(i) + "-" + str(j) + " ") #For checking the indexation
        pass
"""

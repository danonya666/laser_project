import sys
import datetime
from PIL import Image
sys.path.insert(0, "Lib\site-packages")

f = open('another.txt', 'w')

def is_laser(red_component):
    if(red_component > 70):
        return 1
    else:
        return 0

# should be used like find_laser(im_columns, im_rows, this_pix)
# returns a list with the number of red pixels in every row
def red_component_in_lines(width, height, pix):
    counter = [] # counter of red pixels in a line
        #countring red dots in lines
    for i in range(height):
        counter.append(0) # initializing the lists
        for j in range(width):
            r = pix[j, i][0] # red component of the pixel
            if (is_laser(r)): # if pixel is red enough
                counter[i] += 1

    return counter


# function for returning the place of the laser
def find_laser_matrix_place(counter, height):
    num = 0 # Here we gonna store the position of laser
    square = [] # list of squares of suspicions to laser
    i = 0
    while(i < height):
        if(counter[i]):  # if a line has red dots
            square.append([0, num]) # initializing a place in square list for this object
            while(i < height and counter[i] > 0):
                square[num][0] += counter[i] # counting the square of the object
                i += 1
            num += 1 # going to the next item in square list
        i += 1
    square.sort(reverse = True) # sorting squares, biggest square is in [0]
    return square[0][1] # returning the place of the laser

def find_laser_matrix_centre(pix, counter, position):
    num = 0
    i = 0  # putting i counter to the place of the laser
    while (num != position or counter[i] == 0):
        if (counter[i] > 0):
            i += 1
            while (counter[i] != 0):
                i += 1
            num += 1
        i += 1
    laser_start = -1
    laser_end = -1
    laser_length = -1
    laser_height = -1
    laser_start_i = i
    laser_middle_i = -1
    while(counter[i] > 0):
        laser_height += 1
        i += 1
    laser_middle_i = laser_start_i + laser_height / 2
    j = 0
    r = pix[j, i][0]
    i = laser_middle_i
    while(not is_laser(r)):
        j += 1
        r = pix[j, i][0]
    laser_start = j
    while(is_laser(r)):
        j += 1
        r = pix[j, i][0]
    laser_end = j
    laser_length = laser_end - laser_start
    laser_middle = laser_start + laser_length / 2
    laser_middle_position = [int(laser_middle), int(laser_middle_i), int(laser_length), int(laser_height)]
    return laser_middle_position

# function for returning the medium intensity of the laser
# position - result of the function find_laser_matrix_place
# counter - result of the function find_laser
def medium_intensity(pix, width, height, counter, laser_middle_position):
    num = 0

    red_sum = 0 # sum of the red component in a laser
    pixel_counter = 0 # quantity of pixels in a laser
    intensity = 0 # = red_sum / pixel_counter
    j_start = j = laser_middle_position[0]
    i_start = i = laser_middle_position[1]
    print(laser_middle_position[0], laser_middle_position[1], laser_middle_position[2], laser_middle_position[3])
    while(i < i_start + laser_middle_position[3] / 3): # while we are in the laser
        while(j < j_start + laser_middle_position[2] / 3): # while we are in the row
            while(not is_laser(pix[j, i][0]) and j < width - 1):
                j += 1 # this skips the black dots in a row
            red_sum += pix[j, i][0]
            pixel_counter += 1
            j += 1
        i += 1
        j = 0
    intensity = red_sum / pixel_counter
    return intensity

#print(get_laser_matrix(this_pix, position, im_columns, im_rows, counter)) # printing the intensity
def multiple_images_to_file(quantity, basic_location, name, ending):
    f.write("Logging the changes in laser intensity\n//////////////////")
    for i in range(quantity):
        this_image = Image.open(basic_location + "\\" + name + str(i) + ending)
        this_pix = this_image.load()
        im_columns = this_image.width  # Detect width
        im_rows = this_image.height  # Detect height
        counter = red_component_in_lines(im_columns, im_rows, this_pix)  # the list with the numbers of red dots in each row
        position = find_laser_matrix_place(counter, im_rows)  # the place of the matrix
        current_time = str(datetime.datetime.now())
        laser_middle_position = find_laser_matrix_centre(this_pix, counter, position)
        f.write(str("%.2f" % medium_intensity(this_pix, im_columns, im_rows, counter, laser_middle_position)) + ' - ' + current_time + '\n')   # printing the intensity
    f.write("//////////////////" + '\n' + "end of log")
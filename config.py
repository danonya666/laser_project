import sys
sys.path.insert(0, "libs\Lib\site-packages")
import datetime
import time
from tkinter import *
from PIL import Image
import cv2
f = open('another.txt', 'w')

def is_laser(red_component):
    if(red_component >= 30):
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

def find_laser_matrix_centre(pix, counter, position, im_rows, im_columns):
    num = 0
    i = 0  # putting i counter to the place of the laser
    while (num != position or counter[i] == 0):
        if (counter[i] > 0):
            i += 1
            while (i < im_rows - 1 and counter[i] != 0):
                i += 1
            num += 1
        i += 1
    laser_start = -1
    laser_end = -1
    laser_length = -1
    laser_height = -1
    laser_start_i = i
    laser_middle_i = -1
    while(i < im_rows - 1 and counter[i] > 0):
        laser_height += 1
        i += 1
    laser_middle_i = laser_start_i + laser_height / 2
    j = 0
    r = pix[j, i][0]
    i = laser_middle_i
    while(j < im_columns - 1 and not is_laser(r)):
        j += 1
        r = pix[j, i][0]
    laser_start = j
    while (j < im_columns - 1 and is_laser(r)):
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
    j_start = j = laser_middle_position[0] - laser_middle_position[2] / 3
    i_start = i = laser_middle_position[1] - laser_middle_position[3] / 3
    while(i < laser_middle_position[1] + laser_middle_position[3] / 3): # while we are in the laser
        while(j < laser_middle_position[0] + laser_middle_position[2] / 3): # while we are in the row
            while(not is_laser(pix[j, i][0]) and j < width - 1):
                j += 1 # this skips the black dots in a row
            red_sum += pix[j, i][0]
            pixel_counter += 1
            j += 1
        i += 1
        j = 0
    if pixel_counter > 10:
        intensity = red_sum / pixel_counter
        return intensity
    else:
        error = 0
        return error
#def create_canv():

 #   return canv

def put_dot(x, y, canv, rect_size, Start):
    canv.create_rectangle(Start + x, Start - y, Start + x + rect_size, Start - y - rect_size, outline = "black", fill = "black")


#print(get_laser_matrix(this_pix, position, im_columns, im_rows, counter)) # printing the intensity
def multiple_images_to_file(quantity, basic_location, name, ending):
    #sum41 = []
    f.write("Logging the changes in laser intensity\n//////////////////\n")
    for i in range(quantity):
        this_image = Image.open(basic_location + "\\" + name + str(i) + ending)
        this_pix = this_image.load()
        im_columns = this_image.width  # Detect width
        im_rows = this_image.height  # Detect height
        counter = red_component_in_lines(im_columns, im_rows, this_pix)  # the list with the numbers of red dots in each row
        position = find_laser_matrix_place(counter, im_rows)  # the place of the matrix
        current_time = str(datetime.datetime.now())
        laser_middle_position = find_laser_matrix_centre(this_pix, counter, position, im_rows, im_columns)
        laser_medium_intensity = medium_intensity(this_pix, im_columns, im_rows, counter, laser_middle_position)
        if (not laser_medium_intensity):
            f.write("Laser not found\n")
        else:
            f.write(str("%.2f" % laser_medium_intensity) + ' - ' + current_time + '\n')   # printing the intensity
            #put_dot(time, laser_medium_intensity, canv, 5)

    #mid = []
    #mid = sum41.sort()
    f.write("//////////////////" + '\n' + "end of log")

def auto_image_graph():
    root = Tk()
    camera = cv2.VideoCapture(0)
    it = 0
    canv = Canvas(root, width=1000, height=1000, bg="white")
    canv.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
    canv.create_line(0, 500, 1000, 500, width=2, arrow=LAST)

    First_x = -500
    for i in range(16000):
        if (i % 800 == 0):
            k = First_x + (1 / 16) * i
            canv.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width=0.5, fill='black')
            canv.create_text(k + 515, -10 + 500, text=str(k), fill="purple", font=("Helvectica", "10"))
            if (k != 0):
                canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width=0.5, fill='black')
                canv.create_text(-25 + 500, k + 500, text=str(k), fill="purple", font=("Helvectica", "10"))
        try:
            x = First_x + (1 / 16) * i
            new_f = f.replace('x', str(x))
            y = -eval(new_f) + 500
            x += 500
        except:
            pass
    prev_x = 0
    prev_y = 0

    while True:
        time.sleep(1)
        return_value, image = camera.read()
        # gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('image', image)
        if cv2.waitKey(1) & 0xFF == ord('f'):
            break
        cv2.imwrite('im.png', image)
        print('photo taken ', it)
        it += 2
        this_image = Image.open("im.png")
        this_pix = this_image.load()
        im_columns = this_image.width  # Detect width
        im_rows = this_image.height  # Detect height
        counter = red_component_in_lines(im_columns, im_rows,
                                         this_pix)  # the list with the numbers of red dots in each row
        position = find_laser_matrix_place(counter, im_rows)  # the place of the matrix
        current_time = str(datetime.datetime.now())
        laser_middle_position = find_laser_matrix_centre(this_pix, counter, position, im_rows, im_columns)
        laser_medium_intensity = medium_intensity(this_pix, im_columns, im_rows, counter, laser_middle_position)
        put_dot(it, laser_medium_intensity, canv, 1, 500)
        canv.create_line(500 + prev_x, 500 - prev_y, 500 + it, 500 - laser_medium_intensity, smooth = 1, width = 3, fill = "red")
        prev_x = it
        prev_y = laser_medium_intensity
        canv.pack()
        canv.update()


    root.mainloop()






    #print("in aig")



    camera.release()
    cv2.destroyAllWindows()

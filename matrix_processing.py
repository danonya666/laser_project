from config import *

multiple_images_to_file(50, "screenshots", "dtest", ".png")
this_image = Image.open("check.png")
this_pix = this_image.load()
im_columns = this_image.width  # Detect width
im_rows = this_image.height  # Detect height
counter = red_component_in_lines(im_columns, im_rows, this_pix)
print(find_laser_matrix_centre(this_pix, counter, find_laser_matrix_place(counter, im_rows)))

#this_pix = this_image.load()    #remember, [columns, rows]
"""
im_columns = the number of columns in a picture
im_rows = the number of rows in a picture
"""
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
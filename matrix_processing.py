from config import *

multiple_images_to_file(50, "screenshots", "dtest", ".png")


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
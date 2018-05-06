from config import *
# initialize the camera
camera = cv2.VideoCapture(1)
it = 0
while True:
    time.sleep(1)
    return_value,image = camera.read()
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', image)
    if cv2.waitKey(1)& 0xFF == ord('f'):
        break
    cv2.imwrite('pook/' + 'justatry' + str(it) + '.png' , image)
    print('photo taken ', it)
    it += 1
camera.release()
cv2.destroyAllWindows()

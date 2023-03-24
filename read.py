import cv2 as cv

#reading images

#img =cv.imread('IMAGES/CAR.png')
#cv.imshow('Profile',img)
#cv.waitKey(0)

#Reading Videos

capture=cv.VideoCapture('VIDEOS/video.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) &  0XFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()

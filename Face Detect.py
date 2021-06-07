' Using preloaded pictures in the database of Photos Folder '

import cv2 as cv

#read pictures
img = cv.imread('Photos/av.jpg')

'''# ORIGINAL IMAGE
cv.imshow('Gal', img)'''

#scaling function
def rescaleFrame(frame, scale = 0.65):
    width = int((frame.shape[1]) * scale)
    height = int((frame.shape[0]) * scale)

    dimensions = (width ,height)

    #downgrading interpolation
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)  

#Converting to greyscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey Person', gray)

#read the xml file n store in a variable
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#detect faces with greyscale 
# minNeighbors :- specifies a number of {neighbours} or ractangle to be a face
#DETECT FACES n return the rect co-ordintes as a list to the variable

faces_rect = haar_cascade.detectMultiScale(resized_image, scaleFactor=1.3, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect)}')

#loop over list of co-ordinates of rects n draw rect on faces 
for(x,y,w,h) in faces_rect:
    
    #points n green rect
    cv.rectangle(resized_image, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('Detected faces', resized_image)

#resize
resize = cv.resize(resized_image, (400,300), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

#Edge Cascade
''' canny = cv.Canny(resized_image, 125, 175)
cv.imshow('Canny Edges', canny) '''


cv.waitKey(0)
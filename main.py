import cv2 
import os 

#get image folder 
images_path = input("put the location of your image folder: ")

#list all images in the folder
images = os.listdir(images_path)

#show images with a key press
for image in images:
    img = cv2.imread(os.path.join(images_path, image))
    cv2.imshow('image', img)
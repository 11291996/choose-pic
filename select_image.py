import cv2 
import numpy as np
import os
import natsort

#get the image folder 
address = input("Enter the address of the image folder: ")

#read the image

images = os.listdir(address)
images = natsort.natsorted(images)

idx = 0

images_to_move = []

while True:
    try:
        img = cv2.imread(os.path.join(address, images[idx]))
        cv2.imshow('image', img)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("m"):
            idx += 1
        elif key == ord("n"):
            idx -= 1
        elif key == ord("b"):
            images_to_move.append(images[idx])
            images.pop(idx)
            idx += 1
        else:
            print("Press 'm' to move the next image")
            print("Press 'n' to see the previous image")
        print(f"you have {len(images) - idx} images left and picked {len(images_to_move)} images")
    except IndexError:
        output = input("Enter the name of selected images: ")
        output_dir = os.path.join("/Users/jaewanpark/Downloads/temp/choose-pic/output", output + ".txt")
        with open(output_dir, "w") as f:
            for image in images_to_move:
                directory = os.path.join(address, image)
                f.write(directory + "\n")
        break
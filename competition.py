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
        image1 = cv2.imread(os.path.join(address, images[idx]))
        image2 = cv2.imread(os.path.join(address, images[idx+1]))
        #append black padding to the smaller image
        # Define the desired dimensions for the padded images
        desired_height = max(image1.shape[0], image2.shape[0])
        desired_width = max(image1.shape[1], image2.shape[1])

        # Create black background images with the desired dimensions
        padded_image1 = np.zeros((desired_height, desired_width, 3), dtype=np.uint8)
        padded_image2 = np.zeros((desired_height, desired_width, 3), dtype=np.uint8)

        # Calculate the padding required for each image
        top_pad1 = (desired_height - image1.shape[0]) // 2
        bottom_pad1 = desired_height - image1.shape[0] - top_pad1
        left_pad1 = (desired_width - image1.shape[1]) // 2
        right_pad1 = desired_width - image1.shape[1] - left_pad1

        top_pad2 = (desired_height - image2.shape[0]) // 2
        bottom_pad2 = desired_height - image2.shape[0] - top_pad2
        left_pad2 = (desired_width - image2.shape[1]) // 2
        right_pad2 = desired_width - image2.shape[1] - left_pad2

        # Pad the images with black color
        padded_image1 = cv2.copyMakeBorder(image1, top_pad1, bottom_pad1, left_pad1, right_pad1, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        padded_image2 = cv2.copyMakeBorder(image2, top_pad2, bottom_pad2, left_pad2, right_pad2, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        
        img = np.concatenate((padded_image1, padded_image2), axis=1) 
        cv2.imshow('image', img)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("m"):
            images_to_move.append(images[idx+1])
            idx += 2
        elif key == ord("n"):
            images_to_move.append(images[idx])
            idx += 2
        elif key == ord("b"):
            images_to_move.append(images[idx])
            images_to_move.append(images[idx+1])
            idx += 2
        elif key == ord("v"):
            idx += 2
        else:
            print("Press 'm' to move the image to the next folder")
            print("Press 'n' to see the next image")
        print(f"you have {len(images) - idx} images left and picked {len(images_to_move)} images")
    except IndexError:
        output = input("Enter the name of selected images: ")
        output_dir = os.path.join("/Users/jaewanpark/Downloads/temp/choose-pic/output", output + ".txt")
        with open(output_dir, "w") as f:
            for image in images_to_move:
                directory = os.path.join(address, image)
                f.write(directory + "\n")
        break
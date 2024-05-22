import os 

#move the images to the new folder

#get the image txt file
address = input("Enter the address of the image txt file: ")
images_to_move = []

with open(address, "r", encoding="utf-8") as f:
    images_to_move = f.readlines()



new_folder = input("Enter the address of the new folder: ")
os.makedirs(new_folder, exist_ok=True)

for line in images_to_move:
    line = line.strip()
    #get the image name
    image_name = line.split("/")[-1]
    os.system(f"mv \"{line}\" \"./{new_folder}/{image_name}\"")

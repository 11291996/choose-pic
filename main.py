import gradio as gr 
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

current_image_idx = 0
file_list = None
next_stage_list = []
folder_path = None
image_num = None

#load the images
def load_images(path, num):
    global current_image_idx, file_list, folder_path, next_stage_list, image_num
    image_num = int(num)
    current_image_idx = 0
    next_stage_list = []
    folder_path = path
    file_list = os.listdir(folder_path)
    if len(file_list) < image_num:
        return [], "Not enough images in the folder"
    images = [Image.open(os.path.join(folder_path, file)) for file in file_list[:2]]
    return images, "Upload completed"

def return_images(file_list, images):
    if len(file_list) == 1:
        return images, "You have chosen the last winner!"
    if len(file_list) % 2 == 0:
        return images, f"you are now choosing {len(file_list) // 2} among {len(file_list)}"
    else:
        return images, f"you are now choosing {len(file_list) // 2 } among {len(file_list)} with a walkover"

def choose_left():
    global current_image_idx
    global file_list
    global next_stage_list
    global image_num
    if len(next_stage_list) * 2 + 3 == len(file_list):
        next_stage_list.append(file_list[current_image_idx])
        next_stage_list.append(file_list[current_image_idx + 2])
        if len(next_stage_list) == image_num:
            file_list = next_stage_list[::-1]
            next_stage_list = []
            current_image_idx = 0
            images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
            images, message = return_images(file_list, images)
            return images, f"you finished choosing {image_num} images!"
        """
        To Do: Implement the auto made selection of selected number of images

        if len(next_stage_list) < image_num:
            file_list = next_stage_list[::-1]
            image_num = image_num - len(next_stage_list)
            next_stage_list = [file for file in file_list if file not in next_stage_list]
        """
        file_list = next_stage_list[::-1]
        next_stage_list = []
        current_image_idx = 0
        images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
        images, message = return_images(file_list, images)
        print(file_list)
        return images, message
    if len(next_stage_list) * 2 + 2 == len(file_list):
        next_stage_list.append(file_list[current_image_idx])
        if len(next_stage_list) == image_num:
            file_list = next_stage_list[::-1]
            next_stage_list = []
            current_image_idx = 0
            images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
            images, message = return_images(file_list, images)
            return images, f"you finished choosing {image_num} images!"
        file_list = next_stage_list[::-1]
        next_stage_list = []
        current_image_idx = 0
        images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
        images, message = return_images(file_list, images)
        print(file_list)
        return images, message
    next_stage_list.append(file_list[current_image_idx])
    current_image_idx += 2
    print(file_list[current_image_idx:])
    print(next_stage_list)
    images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
    images, message = return_images(file_list, images)
    return images, message

def choose_right():
    global current_image_idx
    global file_list
    global next_stage_list
    if len(next_stage_list) * 2 + 3 == len(file_list):
        next_stage_list.append(file_list[current_image_idx + 1])
        next_stage_list.append(file_list[current_image_idx + 2])
        if len(next_stage_list) == image_num:
            file_list = next_stage_list[::-1]
            next_stage_list = []
            current_image_idx = 0
            images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
            images, message = return_images(file_list, images)
            return images, f"you finished choosing {image_num} images!"
        file_list = next_stage_list[::-1]
        next_stage_list = []
        current_image_idx = 0
        images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
        images, message = return_images(file_list, images)
        print(file_list)
        return images, message
    if len(next_stage_list) * 2 + 2 == len(file_list):
        next_stage_list.append(file_list[current_image_idx + 1])
        if len(next_stage_list) == image_num:
            file_list = next_stage_list[::-1]
            next_stage_list = []
            current_image_idx = 0
            images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
            images, message = return_images(file_list, images)
            return images, f"you finished choosing {image_num} images!"
        file_list = next_stage_list[::-1]
        next_stage_list = []
        current_image_idx = 0
        images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
        images, message = return_images(file_list, images)
        print(file_list)
        return images, message
    next_stage_list.append(file_list[current_image_idx + 1])
    current_image_idx += 2
    print(file_list[current_image_idx:])
    print(next_stage_list)
    images = [Image.open(os.path.join(folder_path, file)) for file in file_list[current_image_idx:current_image_idx+2]]
    images, message = return_images(file_list, images)
    return images, message

#example for the image folder path: /mnt/f/paneah/dataset/processed/characters/carcion/carcion_colored
with gr.Blocks("Image", "Image") as demo:
    textbox = gr.Textbox(label="Enter the image folder path", value="/mnt/f/paneah/dataset/processed/characters/carcion/temp")
    textbox2 = gr.Textbox(label="Enter the number of images to pick", value=1)
    button = gr.Button("Load Images")
    gallery = gr.Gallery(label="Images")
    with gr.Row():
        button1 = gr.Button("Pic 1", scale=0.5)
        button2 = gr.Button("Pic 2", scale=0.5)
    textbox3 = gr.Textbox(label="Result")
    button.click(load_images, [textbox,textbox2], outputs=[gallery, textbox3])
    button1.click(choose_left, outputs=[gallery, textbox3])
    button2.click(choose_right, outputs=[gallery, textbox3])

if __name__ == "__main__":
    demo.launch(share=True)
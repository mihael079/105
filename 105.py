import os
import cv2

path = "Images"
images = []

for file in sorted(os.listdir(path)):
    name, ext = os.path.splitext(file)

    if ext.lower() in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = os.path.join(path, file)
        print(file_name)
        images.append(file_name)

print(len(images))

if len(images) == 0:
    print("No images found.")
else:
    frame = cv2.imread(images[0])
    height, width, channels = frame.shape
    size = (width, height)
    output = cv2.VideoWriter("Friends.mp4", cv2.VideoWriter_fourcc("m", "p", "4", "v"), 10, size)

    for image in images:
        frame = cv2.imread(image)
        output.write(frame)

    output.release()
    print("Done")


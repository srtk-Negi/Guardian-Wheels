# importing the pygame library
import pygame
import pygame.camera
import os

pygame.camera.init()

# make the list of all available cameras
camlist = pygame.camera.list_cameras()

print(camlist)

# if it exists...
if camlist:
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    image = cam.get_image()
    #pygame.image.save(image, "image.jpg")

    new_folder = "burglar_photos"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    image_path = os.path.join(new_folder, "image.jpg")
    pygame.image.save(image, image_path)

# Print Error Message
else:
    print("No camera on current device")

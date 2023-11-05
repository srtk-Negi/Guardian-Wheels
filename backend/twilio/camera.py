# importing the pygame library
import pygame
import pygame.camera
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

bucket_name = 'guardianwheels'

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

#intialize the s3 
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

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

    try:
        s3.upload_file('burglar_photos/image.jpg', bucket_name, 'uploaded_image.jpg')
        print(f"Image uploaded to {bucket_name}/uploaded_image.jpg")
    except Exception as e:
        print(f"An error occurred: {e}")


# Print Error Message
else:
    print("No camera on current device")



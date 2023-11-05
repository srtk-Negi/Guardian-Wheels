import pygame
import pygame.camera
import os
import boto3
from dotenv import load_dotenv

def capture_and_upload_image():
    load_dotenv()

    bucket_name = 'guardianwheels'

    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    # Initialize the S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    pygame.camera.init()

    # Make a list of all available cameras
    camlist = pygame.camera.list_cameras()

    print(camlist)

    # If a camera exists...
    if camlist:
        cam = pygame.camera.Camera(camlist[0], (640, 480))
        cam.start()
        image = cam.get_image()

        new_folder = "burglar_photos"
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        image_path = os.path.join(new_folder, "image.jpg")
        pygame.image.save(image, image_path)

        data = {
                "user_id": "0001",
                "device_id": "0001",
                "longitude": "32.985503",
                "latitude": "-96.751156",
                "path_to_image": "https://guardianwheels.s3.us-east-2.amazonaws.com/uploaded_image.jpg"
            }

        try:
            s3.upload_file(image_path, bucket_name, 'uploaded_image.jpg')
            print(f"Image uploaded to {bucket_name}/uploaded_image.jpg")
            

            
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No camera on the current device")
        
    return data    
data = capture_and_upload_image()
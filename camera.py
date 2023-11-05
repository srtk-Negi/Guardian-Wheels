# importing the pygame library 
import pygame 
import pygame.camera 

pygame.camera.init() 

# make the list of all available cameras 
camlist = pygame.camera.list_cameras() 

print(camlist)

# if it exists...
if camlist: 

	cam = pygame.camera.Camera(camlist[0], (640, 480)) 
	cam.start() 
	image = cam.get_image() 
	pygame.image.save(image, "filename.jpg") 

# Print Error Message
else: 
	print("No camera on current device") 
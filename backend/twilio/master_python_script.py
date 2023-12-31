import subprocess
import cameraV2
from sensor_to_db import sensor_data_to_db


# Script paths for sending messages to police and the toyota owner
# script1_path = 'C:/Users/Analisa Rojas/Desktop/Hackathons/HackUTD/Guardian-Wheels/backend/twilio/cameraV2.py'
script2_path = '/Users/Sarthak/Desktop/Guardian-Wheels/backend/twilio/user_send_sms.py'
script3_path = '/Users/Sarthak/Desktop/Guardian-Wheels/backend/twilio/user_send_mms.py'
script4_path = '/Users/Sarthak/Desktop/Guardian-Wheels/backend/twilio/police_send_mms.py'

# Run camera and take suspect's photo
# subprocess.run(["python", script1_path])


data_dict = cameraV2.capture_and_upload_image()


# Run the scripts to toyota user and police
subprocess.run(['python', script2_path])

subprocess.run(['python', script3_path])

subprocess.run(['python', script4_path])

sensor_data_to_db(data_dict)

import subprocess

# Script paths for sending messages to police and the toyota owner
script1_path = 'C:/Users/Analisa Rojas/Desktop/Hackathons/HackUTD/Guardian-Wheels/backend/twilio/camera.py'
script2_path = 'C:/Users/Analisa Rojas/Desktop/Hackathons/HackUTD/Guardian-Wheels/backend/twilio/user_send_sms.py'
script3_path = 'C:/Users/Analisa Rojas/Desktop/Hackathons/HackUTD/Guardian-Wheels/backend/twilio/user_send_mms.py'
script4_path = 'C:/Users/Analisa Rojas/Desktop/Hackathons/HackUTD/Guardian-Wheels/backend/twilio/police_send_mms.py'

#Run camera and take suspect's photo
subprocess.run(["python", script1_path])

# Run the scripts to toyota user and police
subprocess.run(['python', script2_path])

subprocess.run(['python', script3_path])

subprocess.run(['python', script4_path])
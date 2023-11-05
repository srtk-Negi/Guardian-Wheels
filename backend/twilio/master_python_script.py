import subprocess

# Script paths for sending messages to police and the toyota owner
script1_path = 'camera.py'
script2_path = 'toyotauser/send_mms.py'
script3_path = 'police/send_mms.py'

#Run camera and take suspect's photo
subprocess.run(["python", script1_path])

# Run the first script in toyota user
subprocess.run(['python', script2_path])

# Run the second script in police
subprocess.run(['python', script3_path])
import subprocess

# Specify the paths to your Python scripts
script1_path = 'toyotauser/send_mms.py'
script2_path = 'police/send_mms.py'

# Run the first script in toyota user
subprocess.run(['python', script1_path])

# Run the second script in police
subprocess.run(['python', script2_path])
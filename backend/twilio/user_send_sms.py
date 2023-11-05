# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='There appears to be suspicious activity near your car. We will keep you updated. View an image here: https://di-uploads-pod10.dealerinspire.com/wilsonvilletoyota/uploads/2019/01/Birds-Eye-View-Above-768x453.png',
         from_='+18443433928',
         to='+12107580135'
     )

print(message.sid)
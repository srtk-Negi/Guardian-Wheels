# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='There appears to be an issue with Analisa Rojas car! She drives a 2015 Silver Toyota Corolla. License plate number SLZ0315. She is parked at this location: https://maps.app.goo.gl/LcqsLBtTWs1X3nxi8 See a live image above.',
        from_='+18443433928',
        media_url=['burglar_photos/image.jpg'],
        to='+12104497471'
    )

print(message.sid)

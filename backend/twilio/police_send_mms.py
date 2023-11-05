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
         body='There appears to be an issue with Analisa Rojas car! She is parked at this location: https://maps.app.goo.gl/LcqsLBtTWs1X3nxi8. She drives a 2015 Silver Toyota Corolla. License plate number SLZ0315.  See a live image here: https://guardianwheels.s3.us-east-2.amazonaws.com/uploaded_image.jpg',
         from_='+18443433928',
         media_url=['https://cdn-apgml.nitrocdn.com/LebpnhtoivqQZrhySxTgIGIqkErReVqW/assets/images/optimized/rev-a4d5476/www.shouselaw.com/wp-content/uploads/2020/06/how-can-a-person-fight-the-charges-in-court.jpg'],
         to='+12104497471'
     )

print(message.sid)

     
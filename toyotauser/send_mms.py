# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC1b64da3f4f91f2ec532d67129fc8c911'
auth_token = "8d27bb8010a05d8868def2d66f7f9fd7"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='There appears to be an issue with your car! We are alerting the authorities. See a live image above.',
         from_='+18443433928',
         media_url=['https://cdn-apgml.nitrocdn.com/LebpnhtoivqQZrhySxTgIGIqkErReVqW/assets/images/optimized/rev-a4d5476/www.shouselaw.com/wp-content/uploads/2020/06/how-can-a-person-fight-the-charges-in-court.jpg'],
         to='+12107580135'
     )

print(message.sid)         
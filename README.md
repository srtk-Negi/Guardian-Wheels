## Inspiration
It was inspired by the tragic events that occurred to our ACM amigo. His car was stolen; lost to the world. BUT!

## What it does
IMAGINE A WORLD, where car burglars feared the Guardian Wheels - an advanced car-burglar alarm system that is triggered via motion and sound. Once triggered, the system turns on alarm lights, takes an internal snapshot of the car; it then forwards this data, along with it's geolocation, details about the car and notifies the police of the robbery in progress. It also notifies the car owner that there is an issue with their car. It also shares this information with a drone that can then further investigate the surrounding area; by taking aerial snapshots and use motion tracking to follow the burglars.

## How we built it
We used Python, Twilio API, an Arduino Grove Board, the laptop camera, a mySQL database, Bootstrap, FastAPI, AWS, JavaScript, HTML, CSS.

## Challenges we ran into
Our team lacked prior experience in hardware-related projects. Delving into the world of hardware for the first time posed a significant learning curve. We also encountered difficulties due to the limitations of our non-programmable drone, adding an extra layer of complexity to the project.

## Accomplishments that we're proud of
We connected all of the pieces! As this is our first venture into hardware, successfully grasping the nuances of Arduino proved to be a significant accomplishment. This encompassed tasks such as incorporating LED lights and a sound sensor within the Arduino IDE, as well as establishing a connection to the primary Python implementation.

## What we learned
We learned about the creation of an API, implementing FastAPI, AWS integration for data management, the intricacies of connecting and programming drones using third-party sources, utilization of the Twilio API, and working with Amazon S3 buckets.

## What's next for Guardian Wheels
Implementation! We would like to make use of our drone to fly towards the longitude and latitude values we are storing in our database. This would help further investigate from an aerial view what is occurring at the scene of the crime. Ideally, this would also be able to track fleeing subjects and help police track down burglars in a more effective matter.

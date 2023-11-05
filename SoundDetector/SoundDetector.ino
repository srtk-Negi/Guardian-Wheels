/*This programs takes in sounds, determines if it meets the broken glass thresshold, and returns the state of the car. If car is broken into, it will return a 1*/

int soundPin = A2; // Analog sound sensor is to be attached to analog
int ledPin = 4; // Digital LED is to be attached to digital
int brokenGlassThresshold = 800; //Regconizing this is a broken glass noise 
void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int soundState = analogRead(soundPin); // Read sound sensor’s value
 // Serial.println(soundState);   
  if (soundState > brokenGlassThresshold)
  {
    Serial.println("1");
    for(int i = 0; i<50; i++){
      digitalWrite(ledPin, HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(100);                      // wait for a second
      digitalWrite(ledPin, LOW);   // turn the LED off by making the voltage LOW
      delay(100); 
    }
  }
  else
  {
    digitalWrite(ledPin, LOW); // light remains off while there's no noise
  }
}



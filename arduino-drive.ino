/*
   Remote control

   09/20/2016
   Author: Xiang (Peter) Wang
*/
/*
#include <Servo.h>
#define MIN 1250
#define MAX 1750
#define STOP 1500

Servo myservo1;
Servo myservo2;

int right_wheel_pin = 10;
int left_wheel_pin = 9;

int right_value = STOP;
int left_value = STOP;

void setup()
{
  // attach pins
  myservo1.attach(right_wheel_pin);
  myservo2.attach(left_wheel_pin);
  // initialize wheel position
  myservo1.writeMicroseconds(STOP);
  myservo2.writeMicroseconds(STOP);
  // initialize serial
  Serial.begin(9600);
  Serial.println("Setup completed...");
  Serial.println("Please use w,a,s,d to send control signal...");
}

void loop()
{
  // myservo1.writeMicroseconds(MIN); //full forward
  // myservo1.writeMicroseconds(STOP); //stop
  // myservo1.writeMicroseconds(MAX); //full reverse
  myservo1.writeMicroseconds(left_value);
  myservo2.writeMicroseconds(right_value);

  delay(500);
}

void serialEvent()
{
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    Serial.println(inChar);
    if (inChar == 'a')
    {
      right_value = MIN;
    }
    else if (inChar == 'd')
    {
      left_value = MIN;
    }
    else if (inChar == 'w')
    {
      left_value = MIN;
      right_value = MIN;
    }
    else if (inChar == 's')
    {
      left_value = MAX;
      right_value = MAX;
    }
    else if (inChar == 'q')
    {

    }
    else if (inChar == 'e')
    {

    }
  }
}
*/
#include <Servo.h>
#define MIN 1250
#define MAX 1750
#define STOP 1500
Servo myservo1; // create servo object to control a RoboClaw channel
Servo myservo2; // create servo object to control a RoboClaw channel
int pos = 0; // variable to store the servo position
void setup()
{
 myservo1.attach(5); // attaches the RC signal on pin 5 to the servo object
 myservo2.attach(6); // attaches the RC signal on pin 6 to the servo object
}
void loop()
{
 myservo1.writeMicroseconds(STOP); //Stop
 myservo2.writeMicroseconds(STOP); //Stop
 delay(2000);
 myservo1.writeMicroseconds(MIN); //full forward
 delay(1000);
 myservo1.writeMicroseconds(STOP); //stop
 delay(2000);
 myservo1.writeMicroseconds(MAX); //full reverse
 delay(1000);
 myservo1.writeMicroseconds(STOP); //Stop
 delay(2000);
 myservo2.writeMicroseconds(MIN); //full turn left
 delay(1000);
 myservo2.writeMicroseconds(STOP); //Stop
 delay(2000);
 myservo2.writeMicroseconds(MAX); //full turn right
 delay(1000);
} 


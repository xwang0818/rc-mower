/*
 * Remote control
 * 
 * 09/20/2016
 * Author: Xiang (Peter) Wang
 */


// motor one
const int in1 = 3;
const int in2 = 9;

// motor two
const int in3 = 5;
const int in4 = 6;

int right_value = 0;
int left_value = 0;
int forward_value = 0;
int backward_value = 0;

void setup() 
{
  // initialize serial
  Serial.begin(9600);

  // initialize motor values
  analogWrite(in1, 0);
  analogWrite(in2, 0);
  analogWrite(in3, 0);
  analogWrite(in4, 0);

  Serial.println("Setup completed...");
  Serial.println("Please use a,d,w,s to control the car...");
}


void loop() 
{
    analogWrite(in3, left_value);
    analogWrite(in4, right_value);
    analogWrite(in1, forward_value);
    analogWrite(in2, backward_value);
    
    right_value = 0;
    left_value = 0;
    forward_value = 0;
    backward_value = 0;

    delay(500);
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() 
{
  while (Serial.available()) 
  {
    char inChar = (char)Serial.read();
    Serial.println(inChar);
    if (inChar == 'a')
    {
      left_value = 255;
    }
    else if(inChar == 'd')
    {
      right_value = 255;
    }
    else if(inChar == 'w')
    {
      forward_value = 255;
    }
    else if(inChar == 's')
    {
      backward_value = 255;
    }
    else if(inChar == 'q')
    {
      forward_value = 255;
      left_value = 255;
    }
    else if(inChar == 'e')
    {
      forward_value = 255;
      right_value = 255;
    }    
  }
}


// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);

int sensorRightPin = A3;
int sensorCenterPin = A1;
int sensorLeftPin = A2;
int sensorLeft = 0;        // value read from the pot
int sensorCenter = 0;
int sensorRight = 0;
int Porog = 400; //int Porog = 650;
int shrjadardz = 300;

void setup() {

  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motor
  motor1.setSpeed(150);
  motor1.run(RELEASE);
  motor2.setSpeed(150);
  motor2.run(RELEASE);
}

void loop() {

  readsensors();
  
  RunRobot();
}


void RunRobot()
{
  if ((sensorCenter > Porog) && (sensorLeft < Porog) && (sensorRight < Porog)) {
    GnalAraj();
  }

  if ((sensorLeft > Porog) && (sensorCenter < Porog) && (sensorRight < Porog)) {
    GnalDzax();
  }

  if ((sensorRight > Porog) && (sensorLeft < Porog) && (sensorCenter < Porog)) {
    GnalAj();
  }

  if ((sensorCenter > Porog) && (sensorLeft > Porog) && (sensorRight > Porog)) {
    Kangnel();
  }


  if ((sensorCenter < Porog) && (sensorLeft < Porog) && (sensorRight < Porog)) {
    //Pttvel();
  }

  delay(20);

}

void readsensors ()
{
  sensorLeft = analogRead(sensorLeftPin);
  sensorCenter = analogRead(sensorCenterPin);
  sensorRight = analogRead(sensorRightPin);
  Serial.print("left = ");
  Serial.print(sensorLeft);
  Serial.print("\t Center = ");
  Serial.print(sensorCenter);
  Serial.print("\t right = ");
  Serial.println(sensorRight);
}

void GnalAraj()
{
  motor1.setSpeed(150);
  motor2.setSpeed(150);
  while ((sensorLeft < Porog) && (sensorRight < Porog))
  {
    motor1.run(FORWARD);
    motor2.run(FORWARD);
    readsensors();
  }
}

void GnalAj()
{
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  int i = 50;
  while ((sensorCenter < Porog) && (sensorLeft  < Porog))
  {
    if (i <= 100)
    {
      i = i + 10;
    }
    motor1.setSpeed(i);
    motor2.setSpeed(i);
    motor1.run(FORWARD);
    motor2.run(BACKWARD);
    readsensors();
  }
  motor1.setSpeed(150);
  motor2.setSpeed(150);

}

void GnalDzax()
{
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  int i = 50;
  while ((sensorCenter < Porog) && (sensorRight < Porog))
  {
    if (i <= 100)
    {
      i = i + 10;
    }
    motor1.setSpeed(i);
    motor2.setSpeed(i);
    motor1.run(BACKWARD);
    motor2.run(FORWARD);
    readsensors();
  }
  motor1.setSpeed(150);
  motor2.setSpeed(150);
}

void Kangnel()
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  readsensors();
};


void Pttvel()
{
  while ((sensorCenter < Porog))
  {
    motor1.run(BACKWARD);
    motor2.run(FORWARD);
    readsensors();
  }
}



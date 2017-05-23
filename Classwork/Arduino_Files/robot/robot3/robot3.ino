// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>


AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);

int sensorRightPin = A3;
int sensorCenterPin = A1;
int sensorLeftPin = A2;
int sensorLeft = 0;        // value read from the pot
int sensorCenter = 0;
int sensorRight = 0;
int Porog = 525; 
//int Porog = 650;
int araj = 150;
int shrjadardz = 95;
int Trig = 2;
int Echo = 13;
int runonce = 0;
int SpaseluJamanak = 200;

unsigned int impulseTime = 0;
unsigned int distance_sm = 0;


void setup() {

  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motor
  motor1.setSpeed(150);
  motor1.run(RELEASE);
  motor2.setSpeed(150);
  motor2.run(RELEASE);
  motor3.setSpeed(150);
  motor3.run(RELEASE);

  pinMode(Trig, OUTPUT); //инициируем как выход
  pinMode(Echo, INPUT); //инициируем как вход
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
    GnalAj();
  }

  if ((sensorRight > Porog) && (sensorLeft < Porog) && (sensorCenter < Porog)) {
    GnalDzax();
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
  motor1.setSpeed(araj);
  motor2.setSpeed(araj);
  while ((sensorLeft < Porog) && (sensorRight < Porog))
  {
    motor1.run(FORWARD);
    motor2.run(FORWARD);
    readsensors();
  }
}

void GnalDzax()
{
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  int i = 50;
  while ((sensorCenter < Porog) && (sensorLeft  < Porog))
  {
    if (i <= shrjadardz)
    {
      i = i + 10;
      delay(SpaseluJamanak);
    }
    motor1.setSpeed(i);
    motor2.setSpeed(i);
    motor1.run(FORWARD);
    motor2.run(BACKWARD);
    readsensors();
  }
  motor1.setSpeed(araj);
  motor2.setSpeed(araj);

}

void GnalAj()
{
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  int i = 50;
  while ((sensorCenter < Porog) && (sensorRight < Porog))
  {
    if (i <= shrjadardz)
    {
      i = i + 10;
      delay(SpaseluJamanak);
    }
    motor1.setSpeed(i);
    motor2.setSpeed(i);
    motor1.run(BACKWARD);
    motor2.run(FORWARD);
    readsensors();
  }
  motor1.setSpeed(araj);
  motor2.setSpeed(araj);
}

void Kangnel()
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  readsensors();
  mkrattvox();
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

int Heravorutyun()
{
  digitalWrite(Trig, HIGH);
  /* Подаем импульс на вход trig дальномера */
  delayMicroseconds(10); // равный 10 микросекундам
  digitalWrite(Trig, LOW); // Отключаем
  impulseTime = pulseIn(Echo, HIGH); // Замеряем длину импульса
  distance_sm = impulseTime / 58; // Пересчитываем в сантиметры
  return distance_sm;
}


void mkrattvox()
{
  while (1)
  {
    int dzerq = Heravorutyun();
    if (dzerq < 20)
    {
      delay(3000);
      dzerq = Heravorutyun();
      if (dzerq < 20)
      {
        delay(1000);
        tal_mkrat_mek_angam();
      }
    }
  }
}

void tal_mkrat_mek_angam()
{
  if (runonce <= 2)
  {
    Serial.println("mkraty tveci ");
    motor3.setSpeed(150);
    motor3.run(BACKWARD);
    delay(1000);
    motor3.run(RELEASE);
    delay(1000);
    motor3.run(FORWARD);
    delay(1000);
    motor3.run(RELEASE);
    runonce = runonce + 1;
  }
}


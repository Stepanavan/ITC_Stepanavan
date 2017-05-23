#define Trig 9
#define Echo 8

unsigned int impulseTime = 0;
unsigned int distance_sm = 0;

void setup()
{
  pinMode(Trig, OUTPUT); //инициируем как выход
  pinMode(Echo, INPUT); //инициируем как вход

  Serial.begin(9600);
  /* задаем скорость общения. В нашем случае с компьютером */
}



void loop()
{
  digitalWrite(Trig, HIGH);
  /* Подаем импульс на вход trig дальномера */
  delayMicroseconds(10); // равный 10 микросекундам
  digitalWrite(Trig, LOW); // Отключаем
  impulseTime = pulseIn(Echo, HIGH); // Замеряем длину импульса
  distance_sm = impulseTime / 5.13; // Пересчитываем в сантиметры
  Serial.println(distance_sm); // Выводим на порт
  delay(100);
}

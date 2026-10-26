#include <Servo.h>
Servo s1;

int testAngles[] = {90,60,90,120,90,45,90,135,90,0,90,180,90};

void setup() {
  s1.attach(9);
  Serial.begin(9600);
  Serial.println("angle"); // заголовок csv
}

void loop() {
  for(int i=0; i<13; i++){
    s1.write(testAngles[i]);
    Serial.println(testAngles[i]); // пишет в монитор порта твой csv
    delay(1000); // 1 сек на каждую позицию
  }
}

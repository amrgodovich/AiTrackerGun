#include <Servo.h>

Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(115200);
  servoX.attach(4);
  servoY.attach(6);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    
    if (commaIndex != -1) {
      int angleX = data.substring(0, commaIndex).toInt();
      int angleY = data.substring(commaIndex + 1).toInt();
      
      // Move the servo motors based on received angles
      servoX.write(angleX);
      servoY.write(angleY);
    }
  }
}

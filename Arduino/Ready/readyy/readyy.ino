#include <Servo.h>

Servo servo_y;
Servo servo_x;
void setup() {
 Serial.begin(115200);

  // Attach the servo motors to the pins
  servo_x.attach(4);
  servo_x.write(66.5);
  servo_y.attach(6);
  servo_y.write(110);
}

// the loop function runs over and over again forever
void loop() {
 
}

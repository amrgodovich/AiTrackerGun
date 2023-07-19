# AiTrackerGun
We can divide the project into three main parts:

Part 1: Webcam and Face Detection
The first part involves using a webcam to capture images of passing targets. The webcam performs face detection and sends the coordinates of the detected target to a computer running Python code. Suitable mathematical calculations are performed on the computer to determine the required angles for moving the weapon.

Part 2: Microcontroller
In this project, an Arduino Mega microcontroller is used. It is connected to the computer to receive the target coordinates. The microcontroller is also connected to a laser used in the weapon, as well as two servo motors. The servo motors are responsible for moving the weapon based on the calculated angles.

Part 3: Servo Motors
Two servo motors are used in the project. Servo motors are known for their circular motion based on specific angles. One servo motor is used to control the movement along the X-axis, while the other controls the movement along the Y-axis. By using these servo motors, a network of points is formed to cover all possible target positions.

To achieve project accuracy, several experiments were conducted to determine the available angles in front of the camera. It was determined that the X-axis angle ranges from 37 to 97 degrees, while the Y-axis angle ranges from 90 to 130 degrees.

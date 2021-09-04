#include <Arduino_APDS9960.h>
#include <Arduino_LSM9DS1.h>

float x, y, z;

int plusThreshold = 90, minusThreshold = -90;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);

  while (!Serial);
  if (!APDS.begin()) {
    Serial.println("Error Initialising sensor");
  }

  Serial.println("Detecting Gestures");
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
  }

  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Gyroscope in degrees/second");

}

void loop() {
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z);
  }

  if(y > plusThreshold)
  {
    Serial.println("Moving back");
    delay(2000);
  }
  if(y < minusThreshold)
  {
    Serial.println("Moving front");
    delay(2000);
  }
  if(x < minusThreshold)
  {
    Serial.println("Moving left");
    delay(2000);
  }
    if(x > plusThreshold)
  {
    Serial.println("Moving right");
    delay(2000);
  }
    if (APDS.gestureAvailable()) {
    // a gesture was detected, read and print to serial monitor
    int gesture = APDS.readGesture();

    switch (gesture) {
      case GESTURE_UP:
        Serial.println("Detected UP gesture");
        digitalWrite(LEDR, LOW);
        delay(1000);
        digitalWrite(LEDR, HIGH);
        break;

      case GESTURE_DOWN:
        Serial.println("Detected DOWN gesture");
        digitalWrite(LEDG, LOW);
        delay(1000);
        digitalWrite(LEDG, HIGH);
        break;

      default:
        // ignore
        break;
    }
  }
}

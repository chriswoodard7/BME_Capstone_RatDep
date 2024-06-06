#include "Bitcraze_PMW3901.h"

// Using digital pin 10 for chip select
Bitcraze_PMW3901 flow(10);

void setup() {
  Serial.begin(9600);

  if (!flow.begin()) {
    Serial.println("Initialization of the flow sensor failed");
    while(1) { }
  }
}

int16_t deltaX,deltaY,pir1,pir2,pir3,pir4;

void loop() {
  // Get motion count since last call
  flow.readMotionCount(&deltaX, &deltaY);
  pir1 = digitalRead(5);
  pir2 = digitalRead(6);
  pir3 = digitalRead(3);
  pir4 = digitalRead(4);

  Serial.print(deltaX);
  Serial.print(",");
  Serial.print(deltaY);
  Serial.print(",");
  Serial.print(pir1);
  Serial.print(",");
  Serial.print(pir2);
  Serial.print(",");
  Serial.print(pir3);
  Serial.print(",");
  Serial.print(pir4);
  Serial.print("\n");

  delay(100);
}

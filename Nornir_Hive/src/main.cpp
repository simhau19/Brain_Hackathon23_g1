#include <Arduino.h>
#include "hive.h"

void setup() {
  Serial.begin(115200);
  wifi_setup();
}

void loop() {
  hive_listen();
}
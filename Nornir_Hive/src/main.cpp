#include <Arduino.h>
#include "hive.h"
#include "sensors.h"



void setup() {
  Serial.begin(115200);
  hive_init();
}

void loop() {
  if(ws_channel.available()) {
        ws_channel.poll();
    }
  
  hive_transmit(String(temp_get()));
  delay(500);
}
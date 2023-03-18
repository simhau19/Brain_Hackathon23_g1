#include "sensors.h"
#include <OneWire.h>
#include <DallasTemperature.h>

OneWire one_wire(TEMP_DATA_PIN);
DallasTemperature temp_sensor(&one_wire);

void temp_init(){
    temp_sensor.begin();
}

float temp_get(){
    temp_sensor.requestTemperatures();
    return temp_sensor.getTempCByIndex(0);
}
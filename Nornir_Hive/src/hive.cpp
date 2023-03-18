#include "hive.h"
#include "Arduino.h"
#include "ArduinoHttpClient.h"
#include "WiFi.h"
#include "WiFiClientSecure.h"

void wifi_setup(){
    WiFi.begin(WIFI_SSID, WIFI_PASSWD);
    Serial.print("Connecting to wifi");

    while(WiFi.status() != WL_CONNECTED){
        Serial.print(".");
        delay(500);
    }

    Serial.println("\nConnected to Wifi!");
}

void hive_listen(){

    if(WiFi.status()== WL_CONNECTED){
        WiFiClient client;

        HttpClient http(client, "https://g1.cioty.com", 80);
        
        Serial.println("making POST request");
        String postData = "token=aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e&objectID=2&format=json";
        http.beginRequest();
        http.post("/test1");
        http.sendHeader("Synx-Cat: 4");
        //http.sendHeader(HTTP_HEADER_CONTENT_TYPE, "application/x-www-form-urlencoded");
        http.endRequest();
        http.write((const byte*)postData.c_str(), postData.length());

        // read the status code and body of the response
        int statusCode = http.responseStatusCode();
        String response = http.responseBody();
        Serial.print("POST Status code: ");
        Serial.println(statusCode);
        Serial.print("POST Response: ");
        Serial.println(response);
    }
}
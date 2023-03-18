#include "hive.h"
#include "Arduino.h"
#include "WiFi.h"

#include <ArduinoJson.h>

WebsocketsClient ws_channel;

void wifi_init() {
    Serial.print("Connecting to ");
    Serial.println(WIFI_SSID);

    WiFi.begin(WIFI_SSID, WIFI_PASSWD);

    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(500);
    }
    Serial.println();
    Serial.println("WiFi Connected!");
}

void handleReceivedMessage(String message) {
    Serial.println(message);
}

void onEventsCallback(WebsocketsEvent event, String data) {
    if(event == WebsocketsEvent::ConnectionOpened) {
        Serial.println("Connnection Opened");
    } else if(event == WebsocketsEvent::ConnectionClosed) {
        Serial.println("Connnection Closed");
    } else if(event == WebsocketsEvent::GotPing) {
        Serial.println("Got a Ping!");
    } else if(event == WebsocketsEvent::GotPong) {
        Serial.println("Got a Pong!");
    }
}

void sendToken() {
    StaticJsonDocument<256> doc;
    JsonObject message = doc.to<JsonObject>();
    message["token"] = HIVE_TOKEN;
    String payload = "";
    serializeJson(message, payload);
    ws_channel.send(payload);
}

void sendServiceURL() {
    StaticJsonDocument<256> doc;
    JsonObject message = doc.to<JsonObject>();
    message["url"] = HIVE_SERVICE "/" HIVE_GHOST_ID;
    String payload = "";
    serializeJson(message, payload);
    ws_channel.send(payload);
}

void ws_init() {
    ws_channel.onMessage([&](WebsocketsMessage message) {
        handleReceivedMessage(message.data());
    });
    ws_channel.onEvent(onEventsCallback);

    ws_channel.setCACert(cert);

    bool connected = ws_channel.connect(HIVE_URL);
    if(connected) {
        Serial.println("Connected!");
        sendToken();
        Serial.println("Token sendt!");
        delay(1000);
        sendServiceURL();
    } else {
        Serial.println("Not Connected!");
        Serial.println("Please restart the device");
    }
}

void hive_init(){
    wifi_init();
    ws_init();
}

void hive_transmit(String data) {
    StaticJsonDocument<256> doc;
    JsonObject message = doc.to<JsonObject>();
    message["DATA"] = data;
    String payload = "";
    serializeJson(message, payload);
    ws_channel.send(payload);

}
#include <MqttCom.h>
#include <Analog.h>
#include <PubSubClient.h>
#include <Servo.h>

const char *ssid = "U+Net4C03";
const char *password = "4000010011";
const char *mqtt_server = "192.168.219.150";

MqttCom com;
Analog cds(A0, 0, 1023, 0, 100);

void publish() {
 char msg[50];
 int water = cds.read();
 com.publish("iot/hong/sensors", water);
}

void setup() {
    com.init(ssid, password);
    com.setServer(mqtt_server, NULL, NULL);
    com.setInterval(2000, publish);
}

void loop() {
    com.run();
}

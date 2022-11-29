// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

// REQUIRES the following Arduino libraries:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

#include "DHT.h"
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <WiFiClientSecure.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
boolean newData = false;


// CAYENNE Configuration 


const byte numChars = 100;
char receivedChars[numChars];

#define CAYENNE_PRINT Serial
#include <CayenneMQTTESP32.h>

char username[] = "84aeb200-6ff7-11ed-8d53-d7cd1025126a";
char password[] = "c36766267423ba1108941490b0428b58c97fd511";
char clientID[] = "316e05e0-6ff8-11ed-8d53-d7cd1025126a";

char ssid[ ] = "Leithy";
char wifiPassword[ ] = "12345678";

#define BOT_TOKEN "5986548034:AAEGFZwnytznxNJ6SR30ZAvgIcUFHC2Zvw4"
WiFiClientSecure secured_client;
UniversalTelegramBot bot(BOT_TOKEN, secured_client);



#define DHTPIN 2     // Digital pin connected to the DHT sensor
// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --
// Pin 15 can work but DHT must be disconnected during program upload.

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 3 (on the right) of the sensor to GROUND (if your sensor has 3 pins)
// Connect pin 4 (on the right) of the sensor to GROUND and leave the pin 3 EMPTY (if your sensor has 4 pins)
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

void slice(const char *str, char *result, size_t start, size_t end)
{
    strncpy(result, str + start, end - start);
}
void initWiFi() {

  const char* ssid = "Leithy";
  const char* password = "12345678";

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
}


void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial2.available() > 0 && newData == false) {
        rc = Serial2.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}



void showNewData() {
    if (newData == true) {
        Serial.print("This just in ... ");
        Serial.println(receivedChars);
        newData = false;
    }
}

void setup() {
  Serial.begin(9600);
  Serial2.begin(115200);
  Serial.println(F("DHTxx test!"));
  //initWiFi();
  Cayenne.begin(username, password, clientID, ssid, wifiPassword);
  secured_client.setCACert(TELEGRAM_CERTIFICATE_ROOT);

 bot.sendMessage("-852390733","Welcome to EzPlant. :) \n Please Choose your plant species: \n 1) Flowers \n 2) Trees \n 3) Fruits \n 4) Shrubs \n","");


  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(500);

  Cayenne.loop();

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);


  recvWithStartEndMarkers(); 
  showNewData(); 

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));

   char buf[100];

   std::string s = receivedChars;

   std::string m = s.substr(0, 4);
   

    Serial.println(std::stof(m)); 
  sprintf(buf, "Current Temperature: %f", t);
  bot.sendMessage("-852390733",buf ,"");
  Cayenne.celsiusWrite(0, t);
  Cayenne.virtualWrite(1, h);
  Cayenne.virtualWrite(2, std::stof(m));

  
}

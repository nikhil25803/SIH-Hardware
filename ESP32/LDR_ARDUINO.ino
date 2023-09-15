  // how bright the LED is

  int sensorPin = 0;
  int sensorValue = 0;
  int LED = 12;

// The setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
}
// The loop function runs over and over again forever
void loop() {
  
  sensorValue = analogRead(sensorPin);
  Serial.print(sensorValue);
  Serial.print("\n");

  if(sensorValue > 300) {
        Serial.println("LIGHT ON");
        digitalWrite(LED, HIGH);
  } else {
        Serial.println("LIGHT DOWN");  
        digitalWrite(LED, LOW);  
  }
  delay(100);
}
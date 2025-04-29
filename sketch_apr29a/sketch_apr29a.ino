const int ledPin = 2;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    int brightness = Serial.parseInt();
    brightness = constrain(brightness, 0, 255);
    analogWrite(ledPin, brightness);
  }
}

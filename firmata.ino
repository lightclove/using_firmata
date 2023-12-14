void setup() {
  Serial.begin(57600);
}

void loop() {
  while (Serial.available() > 0) {
    char incomingChar = Serial.read();
    // Обработка входящего символа, например, вывод в монитор порта
    Serial.print(incomingChar);
  }
}

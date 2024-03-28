/*
  # Example code for the moisture sensor
  # Editor     : Lauren
  # Date       : 13.01.2012
  # Version    : 1.0
  # Connect the sensor to the A0(Analog 0) pin on the Arduino board

  # the sensor value description
  # 0  ~300     dry soil
  # 300~700     humid soil
  # 700~950     in water
*/
int value;

void setup(){
  Serial.begin(57600);

}

void loop(){

  value = analogRead(A0);
  Serial.print("Moisture Sensor Value:");
  Serial.print(value);
  delay(3000);

  if(value > 700) {
    Serial.println("-> in water");
  }
  else if (value > 300) {
    Serial.println("-> humid soil");
  }
  else if (value >= 0) {
    Serial.println("-> dry soil");
  }

}
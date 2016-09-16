int ledPin = 13;
unsigned int data;

void setup() {
Serial.begin(9600);
pinMode(ledPin,OUTPUT);
}


void loop() {
  if (Serial.available() > 0) {
   data = Serial.read();
   if(data == 'Y') digitalWrite(ledPin,HIGH);
   if(data == 'N') digitalWrite(ledPin,LOW);
  }
  
  
  
}

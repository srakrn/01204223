const int piezoA = PIN_PC0;
const int piezoB = PIN_PC1;
const int piezoC = PIN_PC2;
const int piezoD = PIN_PC3;

const int builtinLed = PIN_PD3;

void setup(){
  pinMode(piezoA, INPUT);
  pinMode(piezoB, INPUT);
  pinMode(piezoC, INPUT);
  pinMode(piezoD, INPUT);
  pinMode(builtinLed, OUTPUT);
  
  Serial.begin(9600);
  digitalWrite(builtinLed, LOW);
}

void loop(){
  Serial.print(analogRead(piezoA));
  Serial.print(" ");
  Serial.print(analogRead(piezoB));
  Serial.print(" ");
  Serial.print(analogRead(piezoC));
  Serial.print(" ");
  Serial.print(analogRead(piezoD));
  Serial.println(" ");
}

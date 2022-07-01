int UNIT1 = 2;
int UNIT2 = 3;
int UNIT3 = 4;
int UNIT4 = 5;
int UNIT5 = 6;
int UNIT6 = 7;
int UNIT7 = 8;
int TOWER = 31;

int DIP1 = 53;
int DIP2 = 51;
int DIP3 = 49;
int DIP4 = 47;

void setup() {
  Serial.begin(9600);
  pinMode(UNIT1, OUTPUT);//PWM unit1
  pinMode(UNIT2, OUTPUT);//PWM unit2
  pinMode(UNIT3, OUTPUT);//PWM unit3
  pinMode(UNIT4, OUTPUT);//PWM unit4
  pinMode(UNIT5, OUTPUT);//PWM unit5
  pinMode(UNIT6, OUTPUT);//PWM unit6
  pinMode(UNIT7, OUTPUT);//PWM unit7
  pinMode(TOWER, OUTPUT);//타워 점등을 위한 Digital Output

  pinMode(DIP1, INPUT);//점등 시간 조정을 위한 2진 자리1
  pinMode(DIP2, INPUT);//점등 시간 조정을 위한 2진 자리2
  pinMode(DIP3, INPUT);//점등 시간 조정을 위한 2진 자리3
  pinMode(DIP4, INPUT);//점등 시간 조정을 위한 2진 자리4
}

void loop() {
  while(true){
    Serial.print(digitalRead(DIP1));
    Serial.print("-");
    Serial.print(digitalRead(DIP2));
    Serial.print("-");
    Serial.print(digitalRead(DIP3));
    Serial.print("-");
    Serial.println(digitalRead(DIP4));
    delay(1000);

    /*
    //Default 동작, 전체 웨이브
    for(int i=0; i<255; i++){
      analogWrite(UNIT1, i);
      analogWrite(UNIT2, i);
      analogWrite(UNIT3, i);
      analogWrite(UNIT4, i);
      analogWrite(UNIT5, i);
      analogWrite(UNIT6, i);
      analogWrite(UNIT7, i);
  
      Serial.println(i);
      delay(10);   
    }*/
    /*
    for(int i=255; i>0; i--){
      analogWrite(led_pin, i);
      Serial.println(i);
      delay(100);
    }*/
  }
}

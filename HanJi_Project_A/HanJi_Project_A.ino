int UNIT1 = 2;
int UNIT2 = 3;
int UNIT3 = 4;
int UNIT4 = 5;
int UNIT5 = 6;
int UNIT6 = 7;
int UNIT7 = 8;
int TOWER = 31;

int DIP1 = 47;
int DIP2 = 49;
int DIP3 = 51;
int DIP4 = 53;

int LIGHT_TIME(int pin4, int pin3, int pin2, int pin1){
  int T=0;
  if (pin4==0 && pin3==0 && pin2==0 && pin1==1)
  return T=1;
  if (pin4==0 && pin3==0 && pin2==1 && pin1==0)
  return T=2;
  if (pin4==0 && pin3==0 && pin2==1 && pin1==1)
  return T=3;
  if (pin4==0 && pin3==1 && pin2==0 && pin1==0)
  return T=4;
  if (pin4==0 && pin3==1 && pin2==0 && pin1==1)
  return T=5;
  if (pin4==0 && pin3==1 && pin2==1 && pin1==0)
  return T=6;
  if (pin4==0 && pin3==1 && pin2==1 && pin1==1)
  return T=7;
  if (pin4==1 && pin3==0 && pin2==0 && pin1==0)
  return T=8;
  if (pin4==1 && pin3==0 && pin2==0 && pin1==1)
  return T=9;
  if (pin4==1 && pin3==0 && pin2==1 && pin1==0)
  return T=10;
  if (pin4==1 && pin3==0 && pin2==1 && pin1==1)
  return T=11;
  if (pin4==1 && pin3==1 && pin2==0 && pin1==0)
  return T=12;
  if (pin4==1 && pin3==1 && pin2==0 && pin1==1)
  return T=13;
  }
        
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
    //LIGHT_TIME(digitalRead(DIP4), digitalRead(DIP3), digitalRead(DIP2), digitalRead(DIP1));
    //Default 동작, 전체 웨이브
    for(int i=0; i<255; i++){
      Serial.println(LIGHT_TIME(digitalRead(DIP4), digitalRead(DIP3), digitalRead(DIP2), digitalRead(DIP1)));
      Serial.print(digitalRead(DIP4));
      Serial.print(digitalRead(DIP3));
      Serial.print(digitalRead(DIP2));
      Serial.println(digitalRead(DIP1));
      analogWrite(UNIT1, i);
      /*analogWrite(UNIT2, i);
      analogWrite(UNIT3, i);
      analogWrite(UNIT4, i);
      analogWrite(UNIT5, i);
      analogWrite(UNIT6, i);
      analogWrite(UNIT7, i);*/
      delay(10);   
      }
    for(int i=255; i>0; i--){
      analogWrite(UNIT1, i);
      /*
      analogWrite(UNIT2, i);
      analogWrite(UNIT3, i);
      analogWrite(UNIT4, i);
      analogWrite(UNIT5, i);
      analogWrite(UNIT6, i);
      analogWrite(UNIT7, i);*/
      delay(10);
      }
    }
  
}

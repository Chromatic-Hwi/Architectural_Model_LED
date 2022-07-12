int UNIT1 = 2;
int UNIT2 = 3;
int UNIT3 = 4;
int UNIT4 = 5;
int UNIT5 = 6;
int UNIT6 = 7;
int UNIT7 = 8;

int PWM = 9;

int TOWER = 31;

int INPUT1 = 24;
int INPUT2 = 26;
int INPUT3 = 28;
int INPUT4 = 30;
int INPUT5 = 32;
int INPUT6 = 34;
int INPUT7 = 36;

int SET = 40;

void setup() {
  Serial.begin(9600);
  pinMode(PWM, OUTPUT);//PWM unit1
  pinMode(TOWER, OUTPUT);//타워 점등을 위한 Digital Output

  pinMode(INPUT1, INPUT);
  pinMode(INPUT2, INPUT);
  pinMode(INPUT3, INPUT);
  pinMode(INPUT4, INPUT);
  pinMode(INPUT5, INPUT);
  pinMode(INPUT6, INPUT);
  pinMode(INPUT7, INPUT);
  pinMode(SET, INPUT);
}

void loop() {
  //여기서 라즈베리에서 받은 조건을 문자열로 정의해서 돌려야 함.
  // 왜냐하면 라즈베리의 출력 7개는 아두이노에서 제어를 못하기 때문에 pwm이냐/아니냐의 신호만 받아야 한다.
  //라즈베리에서 버튼이 입력되지 않는 default 상태는 pwm이라는 상태 정의 신호를 아두이노한테 보내서 default 동작인 pwm을 하도록 하고
  //라즈베리에서 버튼 입력이 오면 시간 지연+특정 포트 릴레이 작동, 인터럽트에 주목하지 말고 조금 씹히는 여유를 인정할것.
  
  while(true){
    if (digitalRead(SET)==0);{
      
      for(int i=0; i<255; i++){
        analogWrite(PWM, i);
        delay(5);

        if (digitalRead(SET)==1){
          Serial.println("PWM 정지");
          analogWrite(PWM, 0);
          break;
          }
        }
        
      if (digitalRead(INPUT1)==1){
        Serial.println("1번 작동");
        analogWrite(UNIT1, 250);
        delay(5000);
        analogWrite(UNIT1, 0);
        delay(1);
        }
      else if (digitalRead(INPUT2)==1){
        Serial.println("2번 작동");
        analogWrite(UNIT2, 250);
        delay(5000);
        analogWrite(UNIT2, 0);
        delay(1);
        }
      else if (digitalRead(INPUT3)==1){
        Serial.println("3번 작동");
        analogWrite(UNIT3, 250);
        delay(5000);
        analogWrite(UNIT3, 0);
        delay(1);
        }
      else if (digitalRead(INPUT4)==1){
        Serial.println("4번 작동");
        analogWrite(UNIT4, 250);
        delay(5000);
        analogWrite(UNIT4, 0);
        delay(1);
        }
      else if (digitalRead(INPUT5)==1){
        Serial.println("5번 작동");
        analogWrite(UNIT5, 250);
        delay(5000);
        analogWrite(UNIT5, 0);
        delay(1);
        }
      else if (digitalRead(INPUT6)==1){
        Serial.println("6번 작동");
        analogWrite(UNIT6, 250);
        delay(5000);
        analogWrite(UNIT6, 0);
        delay(1);
        }
      else if (digitalRead(INPUT7)==1){
        Serial.println("7번 작동");
        analogWrite(UNIT7, 250);
        delay(5000);
        analogWrite(UNIT7, 0);
        delay(1);
        }
      }
        
    for(int i=255; i>0; i--){
      analogWrite(PWM, i);
      Serial.println(digitalRead(SET));
      delay(5);
      
      if (digitalRead(SET)==1){
        Serial.println("PWM 정지");
        analogWrite(PWM, 0);
        break;
        }
      }
      if (digitalRead(INPUT1)==1){
        Serial.println("1번 작동");
        analogWrite(UNIT1, 250);
        delay(5000);
        analogWrite(UNIT1, 0);
        delay(1);
        }
      else if (digitalRead(INPUT2)==1){
        Serial.println("2번 작동");
        analogWrite(UNIT2, 250);
        delay(5000);
        analogWrite(UNIT2, 0);
        delay(1);
        }
      else if (digitalRead(INPUT3)==1){
        Serial.println("3번 작동");
        analogWrite(UNIT3, 250);
        delay(5000);
        analogWrite(UNIT3, 0);
        delay(1);
        }
      else if (digitalRead(INPUT4)==1){
        Serial.println("4번 작동");
        analogWrite(UNIT4, 250);
        delay(5000);
        analogWrite(UNIT4, 0);
        delay(1);
        }
      else if (digitalRead(INPUT5)==1){
        Serial.println("5번 작동");
        analogWrite(UNIT5, 250);
        delay(5000);
        analogWrite(UNIT5, 0);
        delay(1);
        }
      else if (digitalRead(INPUT6)==1){
        Serial.println("6번 작동");
        analogWrite(UNIT6, 250);
        delay(5000);
        analogWrite(UNIT6, 0);
        delay(1);
        }
      else if (digitalRead(INPUT7)==1){
        Serial.println("7번 작동");
        analogWrite(UNIT7, 250);
        delay(5000);
        analogWrite(UNIT7, 0);
        delay(1);
        }
      }
    }
  

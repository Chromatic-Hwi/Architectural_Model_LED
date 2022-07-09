import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#==================================================================
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch1
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch2
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch3
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch4
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch5
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch6
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch7
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch8

"""
# 2진 조합을 통한 점등 시간 조절
GPIO.setup(, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
"""

GPIO.setup(13, GPIO.OUT) #PWM1

GPIO.setup(14, GPIO.OUT) #Unit1
GPIO.setup(15, GPIO.OUT) #Unit2
GPIO.setup(23, GPIO.OUT) #Unit3
GPIO.setup(24, GPIO.OUT) #Unit4
GPIO.setup(25, GPIO.OUT) #Unit5
GPIO.setup(16, GPIO.OUT) #Unit6
GPIO.setup(20, GPIO.OUT) #Unit7
GPIO.setup(21, GPIO.OUT) #Unit8

#===================================================================

WAVE=GPIO.PWM(13, 6000)
WAVE.start(0)

"""
B1=GPIO.input()
B2=GPIO.input()
B3=GPIO.input()
B4=GPIO.input()
# 4-3-2-1 순

if (B4==0 and B3==0 and B2==0 and B1==0):
    SEC=
if (B4==0 and B3==0 and B2==0 and B1==1):
    SEC=1
    
if (B4==0 and B3==0 and B2==1 and B1==0):
    SEC=2
    
if (B4==0 and B3==0 and B2==1 and B1==1):
    SEC=3
    
if (B4==0 and B3==1 and B2==0 and B1==0):
    SEC=4
    
if (B4==0 and B3==1 and B2==0 and B1==1):
    SEC=5
    
if (B4==0 and B3==1 and B2==1 and B1==0):
    SEC=6
    
if (B4==0 and B3==1 and B2==1 and B1==1):
    SEC=7
    
if (B4==1 and B3==0 and B2==0 and B1==0):
    SEC=8
    
if (B4==1 and B3==0 and B2==0 and B1==1):
    SEC=9

if (B4==1 and B3==0 and B2==1 and B1==0):
    SEC=10

2진 조합 결과가 10진 10 이상 부터는 SEC는 동일한 순으로 다시 증가하되, PWM신호의 속도나 밝기를 조절하도록 설정
사용 설명표가 필요할듯 함.
"""
SEC=5

SELECT="wave" #초기 상태 선언

try:
    while(True):
        if SELECT=="wave":
            for DUTY in range(0, 101, 10):
                SW1=GPIO.input(4)
                SW2=GPIO.input(17)
                SW3=GPIO.input(27)
                SW4=GPIO.input(22)
                SW5=GPIO.input(5)
                SW6=GPIO.input(6)
                SW7=GPIO.input(19)
                SW7=GPIO.input(26)
                if SW1==1 or SW2==1 or SW3==1 or SW4==1 or SW5==1 or SW6==1 or SW7==1 or SW8==1:
                    SELECT="unit"
                    break
                WAVE.ChangeDutyCycle(DUTY)
                GPIO.output(13, DUTY)
                time.sleep(0.1)
                
            for DUTY in range(100, -1, -10):
                SW1=GPIO.input(4)
                SW2=GPIO.input(17)
                SW3=GPIO.input(27)
                SW4=GPIO.input(22)
                SW5=GPIO.input(5)
                SW6=GPIO.input(6)
                SW7=GPIO.input(19)
                SW7=GPIO.input(26)
                if SW1==1 or SW2==1 or SW3==1 or SW4==1 or SW5==1 or SW6==1 or SW7==1 or SW8==1:
                    SELECT="unit"
                    break
                WAVE.ChangeDutyCycle(DUTY)
                GPIO.output(13, DUTY)
                time.sleep(0.1)
                
        if SELECT=="unit": 
            WAVE.ChangeDutyCycle(0)
            if SW1==1:
                GPIO.output(14, True)
                time.sleep(SEC)
                GPIO.output(14, False)
            if SW2==1:
                GPIO.output(15, True)
                time.sleep(SEC)
                GPIO.output(15, False)
            if SW3==1:
                GPIO.output(23, True)
                time.sleep(SEC)
                GPIO.output(23, False)
            if SW4==1:
                GPIO.output(24, True)
                time.sleep(SEC)
                GPIO.output(24, False)
            if SW5==1:
                GPIO.output(25, True)
                time.sleep(SEC)
                GPIO.output(25, False)
            if SW6==1:
                GPIO.output(16, True)
                time.sleep(SEC)
                GPIO.output(16, False)
            if SW7==1:
                GPIO.output(20, True)
                time.sleep(SEC)
                GPIO.output(20, False)
            if SW8==1:
                GPIO.output(21, True)
                time.sleep(SEC)
                GPIO.output(21, False)
            else:
                pass
            SELECT="wave"

except KeyboardInterrupt:
    WAVE.stop()
    GPIO.cleanup()
    print("Interruptedd! Exit!")


#GPIO.cleanup()

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

GPIO.setup(14, GPIO.OUT) #Unit1
GPIO.setup(15, GPIO.OUT) #Unit2
GPIO.setup(23, GPIO.OUT) #Unit3
GPIO.setup(24, GPIO.OUT) #Unit4
GPIO.setup(25, GPIO.OUT) #Unit5
GPIO.setup(16, GPIO.OUT) #Unit6
GPIO.setup(20, GPIO.OUT) #Unit7

GPIO.setup(21, GPIO.OUT) #상태 정의

SEC=5

SELECT="wave" #초기 상태 선언

try:
    while(True):
        if SELECT=="wave":
            SW1=GPIO.input(4)
            SW2=GPIO.input(17)
            SW3=GPIO.input(27)
            SW4=GPIO.input(22)
            SW5=GPIO.input(5)
            SW6=GPIO.input(6)
            SW7=GPIO.input(19)
            #print(SW1, SW2, SW3, SW4, SW5, SW6, SW7)
            GPIO.output(21, False)
            
            if SW1==1 or SW2==1 or SW3==1 or SW4==1 or SW5==1 or SW6==1 or SW7==1:
                SELECT="unit"
                time.sleep(0.1)
            
        if SELECT=="unit":
            #print("PWM 명령 중지!\n") 
            GPIO.output(21, True)
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

            else:
                pass
            SELECT="wave"

except KeyboardInterrupt:
    GPIO.cleanup()
    print()
    print("Interruptedd! Exit!")
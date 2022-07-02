import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch2
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch3
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch4
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch5
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch6
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch7

GPIO.setup(13, GPIO.OUT) #PWM1

GPIO.setup(23, GPIO.OUT) #Unit1
GPIO.setup(24, GPIO.OUT) #Unit2
GPIO.setup(25, GPIO.OUT) #Unit3
GPIO.setup(12, GPIO.OUT) #Unit4
GPIO.setup(16, GPIO.OUT) #Unit5
GPIO.setup(20, GPIO.OUT) #Unit6
GPIO.setup(21, GPIO.OUT) #Unit7

GPIO.setup(14, GPIO.OUT) #Tower

WAVE=GPIO.PWM(13, 1000)
WAVE.start(0)

def SWITCH_UNIT(NUM):
     print("Switch{0} Interrupt!!".format(NUM))
     GPIO.output(NUM, True)
     time.sleep(5)
     GPIO.output(NUM, False)
     
#GPIO.add_event_detect(17, GPIO.RISING, callback=SWITCH_UNIT(23), bouncetime=50)
#인터럽트 핀이 기준전압을 다운엣지로 설정했음에도 플로팅 현상이 일어나는것 같음. 하드웨어적으로 해결해야할지 고민 


try:
    while(True):
        for DUTY in range(1, 101, 1):
            WAVE.ChangeDutyCycle(DUTY)
            GPIO.output(13, DUTY)
            print(DUTY)
            time.sleep(0.01)
        for DUTY in range(99, 1, -1):
            WAVE.ChangeDutyCycle(DUTY)
            GPIO.output(13, DUTY)
            print(DUTY)
            time.sleep(0.01)


except KeyboardInterrupt:
    WAVE.stop()
    GPIO.cleanup()
    print("Interruptedd! Exit!")


#GPIO.cleanup()
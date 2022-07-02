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

WAVE=GPIO.PWM(13, 6000)
WAVE.start(0)

SELECT="wave"

try:
    while(True):
        if SELECT=="wave":
            for DUTY in range(1, 101, 10):
                SW1=GPIO.input(17)
                if SW1==1:
                    SELECT="unit"
                    break
                WAVE.ChangeDutyCycle(DUTY)
                GPIO.output(13, DUTY)
                time.sleep(0.1)
                
            for DUTY in range(99, 1, -10):
                if SW1==1:
                    SELECT="unit"
                    break
                WAVE.ChangeDutyCycle(DUTY)
                GPIO.output(13, DUTY)
                time.sleep(0.1)
        if SELECT=="unit": 
            WAVE.ChangeDutyCycle(0)
            GPIO.output(23, True)
            time.sleep(5)
            GPIO.output(23, False)
            SELECT="wave"

except KeyboardInterrupt:
    WAVE.stop()
    GPIO.cleanup()
    print("Interruptedd! Exit!")


#GPIO.cleanup()
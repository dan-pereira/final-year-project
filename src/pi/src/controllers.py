import RPi.GPIO as GPIO
import time

'''
Called From crontab
Turns on water pumps
'''

pins = [14,15,18]
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.HIGH)

def water(pin,s):
    GPIO.output(pin, GPIO.LOW)  # Turn motor on
    time.sleep(s)
    GPIO.output(pin, GPIO.HIGH)  # Turn motor off

if __name__ == '__main__':

    d={0:0.2,1:0.2,2:0.1}
    #TODO read vals from correct location

    try:
        for key,val in d.items():
            pin = pins[key]
            print('pump',key,'run for',val,'seconds')
            water(pin,val)

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

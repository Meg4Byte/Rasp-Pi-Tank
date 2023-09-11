import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

servo_pin = 38

GPIO.setup(servo_pin, GPIO.OUT)

servo_pwm = GPIO.PWM(servo_pin, 50)

# Start the PWM 

servo_pwm.start(2.5)  
tmp = False 

def run_servo():

    global tmp

    if tmp == False :

            print("inside forward")

            servo_pwm.ChangeDutyCycle(2.5)  # 0 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(3.5)  # 45 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(4.5)  # 90 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(5.5)  # 135 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(6.5)  # 180 degrees position
            time.sleep(0.15)

            
            servo_pwm.ChangeDutyCycle(7.5)  # 0 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(8.5)  # 45 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(9.5)  # 90 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(10.5)  # 135 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(11.5)  # 180 degrees position
            time.sleep(0.15)

            tmp = True

    elif tmp == True:


            print("inside reverse")

            servo_pwm.ChangeDutyCycle(10.5)  # 0 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(9.5)  # 45 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(8.5)  # 90 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(7.5)  # 135 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(6.5)  # 180 degrees position
            time.sleep(0.15)

            
            servo_pwm.ChangeDutyCycle(5.5)  # 0 degrees position
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(4.5)  # 45 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(3.5)  # 90 degrees position (center)
            time.sleep(0.15)
            servo_pwm.ChangeDutyCycle(2.5)  # 135 degrees position
            time.sleep(0.15)

            tmp = False


try:
    while True:

        """
        # Move the servo to different positions
        servo_pwm.ChangeDutyCycle(2.5)  # 0 degrees position
        time.sleep(1)
        servo_pwm.ChangeDutyCycle(5.0)  # 45 degrees position (center)
        time.sleep(1)
        servo_pwm.ChangeDutyCycle(7.5)  # 90 degrees position (center)
        time.sleep(1)
        servo_pwm.ChangeDutyCycle(10.0)  # 135 degrees position
        time.sleep(1)
        servo_pwm.ChangeDutyCycle(12.5)  # 180 degrees position
        time.sleep(1)
        """
        run_servo()
        
        
        

except KeyboardInterrupt:
    
    # Clean up and stop the servo PWM
    servo_pwm.stop()
    GPIO.cleanup()

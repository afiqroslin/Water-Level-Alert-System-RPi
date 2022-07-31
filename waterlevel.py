
#Water Level Alert System with Raspberry Pi using ultrasonic sensor
#python code by afiqroslin

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 2
ECHO = 3
i=0

GPIO.setup(TRIG ,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(4 ,GPIO.OUT)
GPIO.setup(23 ,GPIO.OUT)

GPIO.output(TRIG, False)
print("Starting.....")
time.sleep(2)

while True:
   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)

   while GPIO.input(ECHO)==0:
      pulse_start = time.time()

   while GPIO.input(ECHO)==1:
      pulse_stop = time.time()

   pulse_time = pulse_stop - pulse_start

   distance = pulse_time * 17150
   print(round(distance, 2));

   time.sleep(1)
   
   if distance < 3.5: 			#water high, red led blink and buzzer on
       print("WATER LEVEL IS HIGH!")
       GPIO.output(23, False);
       GPIO.output(4, True);
       time.sleep(0.5)
       GPIO.output(4, False);
       time.sleep(0.5)
       GPIO.output(4, True);
       time.sleep(0.5)
       GPIO.output(4, False);
       time.sleep(0.5)
       
   elif distance > 7: 			#water low, red led blink and buzzer on
       print("WATER LEVEL IS LOW")
       GPIO.output(23, False);
       GPIO.output(4, True);
       time.sleep(0.5)
       GPIO.output(4, False);
       time.sleep(0.5)
       GPIO.output(4, True);
       time.sleep(0.5)
       GPIO.output(4, False);
       time.sleep(0.5)

   else:				#optimal water level, green led on, red led off
       GPIO.output(4, False);
       GPIO.output(23, True);

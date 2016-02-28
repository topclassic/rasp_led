import RPi.GPIO as GPIO
import time

def setting():
	GPIO.setmode(GPIO.BCM)
	# 22 RED
	# 23 GREEN
	# 24 BLUE
	GPIO.setup(22,GPIO.OUT)
	GPIO.setup(23,GPIO.OUT)
	GPIO.setup(24,GPIO.OUT)

def main():
	for i in range (0,3):
		GPIO.output(22, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(22, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(24, GPIO.LOW)
		time.sleep(1)
	GPIO.cleanup()

setting()
main()
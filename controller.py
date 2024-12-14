##controller.py
import time
import pyfirmata

comport='/dev/tty0'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:2:o')
led_2=board.get_pin('d:3:o')
led_3=board.get_pin('d:4:o')
led_4=board.get_pin('d:5:o')

def led(emotion):
    if emotion=='happy':
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
    elif emotion=='angry':
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
    elif emotion=='neutral':
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
    elif emotion=='surprise':
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(1)
    else:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)

time.sleep(3)
# Keep the LEDs on for 3 seconds
    
# Turn off all LEDs after 3 seconds
led_1.write(0)
led_2.write(0)
led_3.write(0)
led_4.write(0)
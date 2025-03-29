from machine import Pin
import utime
from utime import sleep_ms,sleep_us,sleep
pulse=Pin(3,Pin.OUT)
echo=Pin(2,Pin.IN)
buzzer=Pin(19,Pin.OUT)
def ultra():
    pulse.value(0)
    sleep_us(2)
    pulse.value(1)
    sleep_us(5)
    pulse.value(0)
    while echo.value() == 0 :
        signaloff=utime.ticks_us()
    while echo.value() == 1 :
        signalon=utime.ticks_us()
    timepassed=signalon-signaloff
    distance=(timepassed*0.0343)/2
    if distance < 50:
        buzzer.value(1)
        utime.sleep_ms(100)
        buzzer.value(0)
        utime.sleep_ms(100)
        print("Obstacle detected! Distance:", distance, "cm")
    else:
        print("The distance from object is ", distance, "cm")
while True:
    ultra()
    utime.sleep(1)
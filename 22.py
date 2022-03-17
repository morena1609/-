import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    
     return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


try:
    while True:
        print("Введите целое число от 0 до 255")
        n = input()
        if n == "q":
            quit()
        if n.isdigit():
            n = int(n)
            if n < 0 or n > 255:
                print("Вы ввели число, выходящее из заданного дипозона. Повторите ввод)")

            else:
                GPIO.output(dac, decimal2binary(n))
                Vout = 3.3 * n / 256
                print("Предполагаемое значение напряжения на выходе:", Vout)
        
        else:
            print("Вы ввели неправильный тип данных. Повторите ввод)")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

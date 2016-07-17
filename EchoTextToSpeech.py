from pyttsx import *
from time import sleep

def main() :
    months = ['August', 'September', 'October', 'November', 'December']
    days = [31, 30, 31, 30, 25]
    monthCounter = 0
    dayCounter = 31
    christmasCounter = 116
    engine = init()

    for month in months :
        while dayCounter <= days[monthCounter] :
            message = ''.join(["alexa, create an event for ", month, " ", str(dayCounter)])
            if dayCounter in [1, 21, 31] :
                message.join("st")
            if dayCounter in [2, 22] :
                message.join("nd")
            if dayCounter in [3, 23] :
                message.join("rd")
            else :
                message.join("th")
            engine.say(message)
            engine.runAndWait()
            sleep(4)
            engine.say(''.join(["all day"]))
            engine.runAndWait()
            sleep(4)
            engine.say(''.join([str(christmasCounter), " days until Christmas"]))
            engine.runAndWait()
            sleep(7)
            engine.say(''.join(["yes"]))
            engine.runAndWait()
            sleep(4)
            christmasCounter -= 1
            dayCounter += 1
        monthCounter += 1
        dayCounter = 1

main()

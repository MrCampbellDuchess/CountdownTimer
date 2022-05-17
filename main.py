import datetime
import cowsay
import time
import os
from config import *


#write a function to clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    present = datetime.datetime.now()
    difference = goaldate - present
    seconds = (round(difference.total_seconds()))
    minutes = round(seconds / 60)
    hours = round(minutes/60,2)
    days = round(hours/24,2)
    weeks = round(days/7,2)

    #this script will only support 4 custom lengths before the text overflows onto another screen
    Len1 = round(minutes/Len1Length,2)
    Len2 = round(minutes/Len2Length,2)
    Len3 = round(minutes/Len3Length,2)
    Len4 = round(minutes/Len4Length,2)
    if seconds <= 0:
        break
    cowsay.milk("There are \n " + str(seconds) + " seconds or \n" + str(minutes) + 
    " minutes or \n" + str(days) + " days or \n " + str(weeks) + " weeks or \n " +
    str(Len1) + " " + Len1Name + "\n" +
    str(Len2) + " " + Len2Name + "\n " +
    str(Len3) + " " + Len3Name + "\n " +
    str(Len4) + " " + Len4Name + "\n " + 
    ' until Summer Break')
    time.sleep(1)
    clear()
cowsay.tux(FinalMessage)

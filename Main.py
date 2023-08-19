import os
from colorama import Fore
import subprocess
import time
err = 0
msg = "0"
lastTemp = 1
temp = 0
percent = 0
counter = 0
colour = Fore.MAGENTA
lastColour = Fore.MAGENTA

print(f"{Fore.LIGHTCYAN_EX}********** {Fore.MAGENTA}Raspberry Pi Temperature App {Fore.LIGHTCYAN_EX}**********{Fore.RESET}")
print(f"                {Fore.LIGHTCYAN_EX}Made By Englishexe{Fore.RESET}                ")
print(f"{Fore.RED}Ignore First Reading{Fore.RESET}")
def getTemp():
        err, msg = subprocess.getstatusoutput("vcgencmd measure_temp") # 0, temp(temp=50'C)
        if err != 0:
                print(f"{Fore.RED}Warning, failed to gather temperature. ({err}){Fore.RESET}")
                exit(1)
        else:
                msg = msg.removeprefix("temp=")
                msg = msg.removesuffix("'C")
                return float(msg)
def getColour(number):
        if number < 20:
                colour = Fore.LIGHTBLUE_EX
        elif number < 50:
                colour = Fore.LIGHTGREEN_EX
        elif number < 80:
                colour = Fore.LIGHTYELLOW_EX
        elif number < 99:
                colour = Fore.RED
        else:
                colour = Fore.MAGENTA
        return colour
while True:
        # temp = getTemp()
        temp = 20
        percent = temp - lastTemp
        percent = percent/lastTemp
        percent = percent * 100
        percent = int(percent)
        if percent < 0:
                percent = f"{Fore.LIGHTBLUE_EX}{percent}%{Fore.RESET}"
        elif percent > 0:
                percent = f"{Fore.LIGHTRED_EX}+{percent}%{Fore.RESET}"
        elif percent == 0:
                percent = f"{Fore.LIGHTGREEN_EX}{percent}%{Fore.RESET}"
        colour = getColour(temp)
        lastColour = getColour(lastTemp)
        print(f"*** Temperature ({counter}) ***\nNew:{colour}{temp}{Fore.RESET}\nOld:{lastColour}{lastTemp}{Fore.RESET}\n{percent}")
        lastTemp = temp
        counter += 1
        time.sleep(5)
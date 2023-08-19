import os
from colorama import Fore
import subprocess
import time
err = 0
msg = "0"
lasttemp = 999
temp = 0
percent = 0
colour = Fore.MAGENTA
lastcolour = Fore.MAGENTA

print(f"{Fore.LIGHTCYAN_EX}********** {Fore.MAGENTA}Raspberry Pi Temperature App {Fore.LIGHTCYAN_EX}**********{Fore.RESET}")
print(f"                {Fore.LIGHTCYAN_EX}Made By Englishexe{Fore.RESET}                ")
print(f"{Fore.RED}Ignore First Reading{Fore.RESET}")
def getTemp():
        err, msg = subprocess.getstatusoutput("vcgencmd measure_temp")
        # msg = "90" # uncomment for debugging
        if err != 0:
                print(f"{Fore.RED}Warning, failed to gather temperature. ({err}){Fore.RESET}")
        else:
                msg = msg.removeprefix("temp=")
                msg = msg.removesuffix("'C")
                return float(msg)
while True:
        temp = getTemp()
        percent = temp - lasttemp
        percent = percent/lasttemp
        percent = percent * 100
        percent = int(percent)
        if percent < 0:
                percent = f"{Fore.LIGHTBLUE_EX}{percent}%{Fore.RESET}"
        elif percent > 0:
                percent = f"{Fore.LIGHTRED_EX}+{percent}%{Fore.RESET}"
        elif percent == 0:
                percent = f"{Fore.LIGHTGREEN_EX}{percent}%{Fore.RESET}"
        if temp < 20:
                colour = Fore.LIGHTBLUE_EX
        elif temp < 50:
                colour = Fore.LIGHTGREEN_EX
        elif temp < 80:
                colour = Fore.LIGHTYELLOW_EX
        elif temp < 99:
                colour = Fore.RED
        else:
                colour = Fore.MAGENTA
        if lasttemp < 20:
                lastcolour = Fore.LIGHTBLUE_EX
        elif lasttemp < 50:
                lastcolour = Fore.LIGHTGREEN_EX
        elif lasttemp < 75:
                lastcolour = Fore.LIGHTYELLOW_EX
        elif lasttemp < 99:
                lastcolour = Fore.RED
        else:
                colour = Fore.MAGENTA
        print(f"*** Temperature ***\nNew:{colour}{temp}{Fore.RESET}\nOld:{lastcolour}{lasttemp}{Fore.RESET}\n{percent}")
        lasttemp = temp
        time.sleep(5)

import subprocess
from datetime import datetime
import time

#defining times
power_on_time = "05:00:00"
power_off_time = "18:00:00"

#off function
def tv_off():
    print("powering off ...")
    time.sleep(1.5)
    subprocess.run(
        'echo standby 0 | cec-client -s -d 1',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )
    time.sleep(5)
    
#on function        
def tv_on():
    subprocess.run(
        'echo on 0 | cec-client -s -d 1',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )
    print("powering on ...")
    time.sleep(5)

#Main function
class Main():
    try:
        time_now = datetime.now().strftime("%H:%M:%S")
        if time_now == power_off_time:
            tv_off()
        elif time_now == power_on_time:
            tv_on()
    except KeyboardInterrupt:
        print("\n",
            "Beende ... ")
        time.sleep(1)
        exit()

#main cycle
if __name__ == "__main__":
    while True:
        Main()

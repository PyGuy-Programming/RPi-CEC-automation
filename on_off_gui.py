import subprocess
from datetime import datetime
import time
import tkinter as tk

#creating window
root = tk.Tk()
root.resizable(False, False)
root.title("CEC-Control-Panel")
root.geometry("300x200")
root.configure(bg="gray")

#temporarily setting stop to False
stop = False

#defining times
power_on_time = "05:00:00"
power_off_time = "18:00:00"

#defining status label
label_status = tk.Label(root, text=" ", bg="gray")    

#off function
def tv_off():
    label_status.config(text="powering off ...")
    def _run2():
        subprocess.run(
            'echo standby 0 | cec-client -s -d 1',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )
    root.after(2000, _run2)
#on function        
def tv_on():
    subprocess.run(
        'echo on 0 | cec-client -s -d 1',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )
    label_status.config(text="powering on ...")

#Main function
def Main():
    time_now = datetime.now().strftime("%H:%M:%S")
    if time_now == power_off_time:
        tv_off()
    elif time_now == power_on_time:
        tv_on()

#definig the Main cycle 
def loop():
    label_status.config(text="starting ...")
    root.after(1500, lambda: label_status.config(text=" "))
    global stop
    
    def _run():
        if not stop:
            Main()
            
            root.after(1000, _run)
    _run()

#defining the stop of the Main cycle
def stoping_loop():
    global stop, label_status
    label_status.config(text="stopping ...")
    root.after(1500, lambda: label_status.config(text=" "))
    stop = True

#defining and packing window, labels and buttons


label1 = tk.Label(root, text="Conrol-Panel", bg="gray")
label1.pack()

labelspacer_1 = tk.Label(root, text=" ", bg="gray")
labelspacer_1.pack()

labelspacer_2 = tk.Label(root, text=" ", bg="gray")
labelspacer_2.pack()

button1 = tk.Button(root, text="START", command=loop, padx=20, bg="blue", fg="white", font=("Courier", 10, "bold"))
button1.pack()

labelspacer_3 = tk.Label(root, text=" ", bg="gray")
labelspacer_3.pack()

button2 = tk.Button(root, text="STOP", command= stoping_loop, padx=23, bg="blue", fg="white", font=("Courier", 10, "bold"))
button2.pack()

label_status.pack()

root.mainloop()
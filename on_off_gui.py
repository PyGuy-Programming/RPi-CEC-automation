#Importing all needed modules
import configparser
import subprocess
from datetime import datetime
import tkinter as tk
import sys
import ttkbootstrap as ttk



#Preparing configparser

config = configparser.ConfigParser()
config.read("config.conf")


#Getting and using some more settings from config.conf

show_current_time = int(config.get("Widgets", "show_current_time"))


#Getting and using some more settings from config.conf

window_size_x = str(config.get("Widgets", "window_size_x"))
window_size_y = str(config.get("Widgets", "window_size_y"))

window_size_x_y = str(window_size_x + "x" + window_size_y)

ttkTheme = str(config.get("Widgets", "ttkTheme"))


#Defining and configuring Window and other things

root = ttk.Window(themename=ttkTheme)
root.geometry(window_size_x_y)
root.title(" ")
root.overrideredirect(int(config.get("Widgets", "unmovable_window")))


#Getting another setting from config.conf

resizable_window = (int(config.get("Widgets", "resizable_window")))
if resizable_window == 1:
    root.resizable(True, True)

elif resizable_window == 0:
    root.resizable(False, False)

sep1 = ttk.Separator(root, orient='horizontal', style="primary.Horizontal.TSeperator")
sep1.pack(fill='x')

title = ttk.Label(sep1, text="CEC-Control-Panel")
title.pack(side="bottom")

sep2 = ttk.Separator(root, orient='horizontal', style="primary.Horizontal.TSeperator")


#Getting on/off-times from config file

power_on_time = str(config.get("Times", "power_on_time"))
power_off_time = str(config.get("Times", "power_off_time"))


#Defining label and String Variable for showing current time

label_time_var = tk.StringVar(value=datetime.now().strftime("%H:%M:%S"))
label_time = ttk.Label(root, textvariable=label_time_var)
label_time_settings1 = ttk.Label(root, text=(f"power on time: {power_on_time}"))
label_time_settings2 = ttk.Label(root, text=(f"power off time: {power_off_time}"))


#Finding out screensize

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#Saving size of window

window_width = int(window_size_x)
window_height = int(window_size_y)


#Calculating middle of screen

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)


#Putting window in middle of screen

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


#Defaulty setting stop to True

stop = True


#Defining status label

label_status = ttk.Label(root, text=" ")    


#Defining off function

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
    
    
#Defining on function
    
def tv_on():
    subprocess.run(
        'echo on 0 | cec-client -s -d 1',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )
    label_status.config(text="powering on ...")
    

#Definig function for closing window and stopping application
    
def close():
    root.destroy()
    sys.exit()
    
    
#Defining main function
    
def main():
    time_now = datetime.now().strftime("%H:%M:%S")
    if time_now == power_off_time:
        tv_off()
    elif time_now == power_on_time:
        tv_on()


#Definig the Main loop
        
def loop():
    global stop
    if stop:
        label_status.config(text="starting .  ")
        root.after(750, lambda: label_status.config(text="starting .. "))
        root.after(1500, lambda: label_status.config(text="starting ..."))
        root.after(2200, lambda: label_status.config(text=" "))
        stop = False
        def _run():
            if not stop:
                main()
                
                root.after(1000, _run)
        _run()
    
    
#Defining the stop of the Main loop
        
def stoping_loop():
    global stop, label_status
    if stop is False:
        label_status.config(text="stopping .  ")
        root.after(750, lambda: label_status.config(text="stopping .. "))
        root.after(1500, lambda: label_status.config(text="stopping ..."))
        root.after(2200, lambda: label_status.config(text=" "))
        stop = True
        
        
#Defining Show_Time
            
def show_time():
    global show_current_time
    if show_current_time == 1:
        root.geometry("350x215")
        label_time.pack_forget()
        label_time_settings1.pack_forget()
        label_time_settings2.pack_forget()
        show_current_time = False
    elif show_current_time == 0:
        root.geometry("350x280")
        label_time.pack()
        label_time_settings1.pack()
        label_time_settings2.pack()
        show_current_time = True


#Defining function for updating the clock
        
def update_clock():
    label_time_var.set(datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_clock)
    
#Defining and packing window, labels and buttons
        
button1 = ttk.Button(root, text="START", command=loop, bootstyle="primary", width=10)
button1.pack(pady=7)

button2 = ttk.Button(root, text="STOP", command=stoping_loop, bootstyle="primary", width=10)
button2.pack(pady=7)

time_on_off = ttk.Button(root, text="Show time", command=show_time, width=10)
time_on_off.pack(pady=7)

sep2.pack(fill='x', pady=10)


label_status.pack(side="bottom")


#Starting update Loop

update_clock()
        
        
# Starting GUI

root.mainloop()

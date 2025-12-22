import subprocess
from datetime import datetime
import tkinter as tk
import sys
import ttkbootstrap as ttk

custom_font_size = 8

show_current_time = False

#creating window
root = ttk.Window(themename="superhero")
root.resizable(False, False)
root.geometry("400x300")
root.title(" ")
root.overrideredirect(False)

sep1 = ttk.Separator(root, orient='horizontal', style="primary.Horizontal.TSeperator")
sep1.pack(fill='x')

title = ttk.Label(sep1, text="CEC-Control-Panel")
title.pack(side="bottom")

sep2 = ttk.Separator(root, orient='horizontal', style="primary.Horizontal.TSeperator")



label_time_var = tk.StringVar(value=datetime.now().strftime("%H:%M:%S"))
label_time = ttk.Label(root, textvariable=label_time_var)

# Bildschirmgröße ermitteln
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Fenstergröße ermitteln
window_width = 350
window_height = 250

# Position berechnen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Geometrie mit der berechneten Position setzen
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#temporarily setting stop to True
stop = True

#defining times
power_on_time = "05:00:00"
power_off_time = "18:00:00"

#defining status label
label_status = ttk.Label(root, text=" ")    


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

#definig function for closing
def close():
    root.destroy()
    sys.exit()
    
#Main function
def Main():
    time_now = datetime.now().strftime("%H:%M:%S")
    if time_now == power_off_time:
        tv_off()
    elif time_now == power_on_time:
        tv_on()

#definig the Main cycle 
def loop():
    global stop
    if stop == True:
        label_status.config(text="starting .  ")
        root.after(750, lambda: label_status.config(text="starting .. "))
        root.after(1500, lambda: label_status.config(text="starting ..."))
        root.after(2200, lambda: label_status.config(text=" "))
        stop = False
        def _run():
            if not stop:
                Main()
                
                root.after(1000, _run)
        _run()
    else:
        pass
    
#defining the stop of the Main cycle
def stoping_loop():
    global stop, label_status
    if stop == False:
        label_status.config(text="stopping .  ")
        root.after(750, lambda: label_status.config(text="stopping .. "))
        root.after(1500, lambda: label_status.config(text="stopping ..."))
        root.after(2200, lambda: label_status.config(text=" "))
        stop = True
    else:
        pass

def show_time():
    global show_current_time
    if show_current_time == True:
        label_time.pack_forget()
        show_current_time = False
    elif show_current_time == False:
        label_time.pack()
        show_current_time = True

#defining and packing window, labels and buttons

button1 = ttk.Button(root, text="START", command=loop, bootstyle="primary", width=10)
button1.pack(pady=7)

button2 = ttk.Button(root, text="STOP", command=stoping_loop, bootstyle="primary", width=10)
button2.pack(pady=7)

time_on_off = ttk.Button(root, text="Show time", command=show_time, width=10)
time_on_off.pack(pady=7)

sep2.pack(fill='x', pady=10)


label_status.pack(side="bottom")

def update_clock():
    global button1, button2, stop
    label_time_var.set(datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_clock)
    
update_clock()
        

root.mainloop()

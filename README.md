## How to change times

  To change the standart¹ on/off times you
  just change the first² time with the time
  you want the TV to turn on and the second³
  time with the time you want the TV to 
  turn off.

  ¹
   ```
   #defining times
   power_on_time = "05:00:00"²
   power_off_time = "18:00:00"³
   ```
## Requirements
  
  - a TV capable of CEC-HDMI
  - Raspberry Pi
  - cec-utils package¹
  - Python-Interpreter¹

¹ installt with apt and following commands
  ```
  sudo apt-get install cec-utils

  sudo apt-get install python3
  ```

## How to
  - click on ```Code``` and then on ```Download ZIP```
  - extract all files from the .zip
  - open terminal and go to your Downloads folder and than to the RPi-CEC-automation-main folder
  - type ```python3 on_off.py``` and it runs

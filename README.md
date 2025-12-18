## Requirements
  
  - a TV capable of CEC-HDMI
  - Raspberry Pi
  - cec-utils package¹
  - Python-Interpreter of choice

¹ installt with apt and following commands
  ```
  sudo apt-get install cec-utils
  ```
## How to

  - press on ```Code``` and then on ```Download ZIP```
  - extract all files from the ZIP file
  - open the .py file in your Python-Interpreter of choice and run the file

## How to change times

   to change time just change the two variabels¹ for the times

   ¹
```
   31  power_on_time = "05:00:00"
   32  power_off_time = "18:00:00"
```

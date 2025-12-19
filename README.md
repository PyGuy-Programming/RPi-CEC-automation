## Requirements
  
  - a TV capable of CEC-HDMI
  - Raspberry Pi
  - cec-utils package¹
  - Python-Interpreter of choice
  - ```ttkbootstrap``` Python-Package²

¹ installt with apt and following commands
  ```
  sudo apt-get install cec-utils
  ```

² install with pip:
  ```
  python3 -m pip install ttkbootstrap
  ```
  if this doesn't work use the following commands:
  ```
  python3 -m venv tutorial_env

  source tutorial_env/bin/activate

  python3 -m pip install ttkbootstrap
  ```

## How to  
  - press on ```Code``` and then on ```Download ZIP```
  - extract all files from the ZIP file
  - open the .py file in your Python-Interpreter of choice and run the file

## How to change times

   to change time just change the two variabels¹ for the times

   ¹
```
   41  power_on_time = "05:00:00"
   42  power_off_time = "18:00:00"
```

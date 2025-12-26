## Requirements
  
  - a TV capable of CEC-HDMI
  - Raspberry Pi
  - cec-utils package¹
  - Python3
  - ```ttkbootstrap``` Python-Package²

¹ Installt with apt and following commands
  ```
  sudo apt-get install cec-utils
  ```

² Install with pip and a virtual env.:
  ```
  python3 -m venv tutorial_env

  source tutorial_env/bin/activate

  python3 -m pip install ttkbootstrap
  ```

## How to
  - press on ```Code``` and then on ```Download ZIP```
  - extract all files from the ZIP file
  - open Terminal and type:
    ```
    source tutorial_env/bin/activate

    cd ~/Downloads/RPi-CEC-automation-main/

    python3 on_off_gui.py
    ```
## How to change times

   To change time just change the two variabels for the times in the config.conf file.

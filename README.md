# linuxgit
Samples of scripts for Linux

# Execute commands in python
https://stackoverflow.com/questions/450285/executing-command-line-programs-from-within-python
https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python

https://docs.python.org/3/library/os.html#os.system

```
import os
os.system('ls')
```


# Simple menu
https://stackoverflow.com/questions/34192588/simple-menu-in-python-3


# JSON
https://www.json.org/

Python JSON
https://www.w3schools.com/python/python_json.asp
```
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 

```
For better printing
```
json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))

```
# Enconding and decoding JSON
https://realpython.com/python-json/

Este parece simple:
https://simplejson.readthedocs.io/en/latest/#


# READ FILES AND STRING IN PYTHON
https://www.pythonforbeginners.com/cheatsheet/python-file-handling/

https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

To read a file line by line, output into a list:
```
with open(“getinfo.txt”) as lol_file: 
cadena_str = lol_file.readlines() 
```
This will take all of the text or content from the “hello.txt” file and store it into a string called “data”.


comprobar esto de abajo....
```
lol_file = open(“getinfo.txt”, “r”) 
cadena_str= lol_file.read() #Al usar read se cierra el vinculo con lol_file  
```
https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files




# Desktop entry specification
Instal desktop Application
```
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal=false
Exec=/path/to/executable
Name=Name of Application
Icon=/path/to/icon
```
Save the file in “~/.local/share/applications” folder as “application-name.desktop”
```
sudo mv ~/.local/share/applications/<application-name.desktop> /usr/share/applications/
```

# Prepare Wifi RASPBERRY

I would not recommend it, but you can run your RaspiBolt with a wireless network connection. To avoid using a network cable for the initial setup, you can pre-configure the wireless settings:

Create a file wpa_supplicant.conf on the MicroSD card with the following content. Note that the network name (ssid) and password need to be in double-quotes (like psk="password")
```
country=[COUNTRY_CODE]
ctrl_interface=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
    ssid="[WIFI_SSID]"
    psk="[WIFI_PASSWORD]"
}
```
    Replace [COUNTRY_CODE] with the ISO2 code of your country (eg. US)
    Replace [WIFI_SSID] and [WIFI_PASSWORD] with the credentials for your own WiFi.


```
```
```
```



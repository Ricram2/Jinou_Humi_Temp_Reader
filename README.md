# Jinou Humi Temp Reader Beacon

Sensor reading for humidity and temperature for JINOU Beacon. JO-BEC09 Python code tested in Headless Raspbian

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installing

Install Bluez on your raspbian, follow this tutorial:

https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation


Turn on your Raspberry Bluetooth after this with:

```
sudo systemctl start bluetooth
```
If you want the bluetooth to keep on every single time the Raspberry turns on enable it as follows:

```
sudo systemctl enable bluetooth
```

### Finding your device's MAC.

This is the most important part, for the code to work you will have to replace the MAC on the code with your device's.

```
sudo hcitool lescan
```

You will see something like this (MAC and the device's name):

```
FF:FF:FF:FF:FF:FF Jinou_Sensor_HumiTemp
```
Save the ```FF:FF:FF:FF:FF:FF``` (MAC) and replace it in the python file.

### Install python packages needed.

Install pexpect to controll gatttools. 

```pip install pexpect```

### Run the code.

```sudo python humi_temp_read.py``` 

## Built With

* [Python](https://www.python.org/downloads/) - Programming language
* [Pexpect](https://pexpect.readthedocs.io/en/stable/) - Python module for controlling other applications in this case gatttool.


## Authors

* **Ricardo Antonio Rambal Fattori** - *Ricram2* - [Github](https://github.com/ricram2)

* **OTHER GUY WHO DID THE MOST** TODO 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

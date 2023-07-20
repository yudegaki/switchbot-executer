# Switchbot executer


## Installation

```
sudo apt-get update
sudo apt-get install python-pexpect
```

## Running
1. Check Your Switch Bot's Mac Address
Switchbot's Mac address can be found on the official app

2. Execute Switch Bot Command

```
$ python exec-switchbot.py -h
usage: exec-switchbot.py [-h] -m MAC -c {TurnOn,TurnOff,Press,Down,Up}

optional arguments:
  -h, --help            show this help message and exit
  -m MAC, --mac MAC     Switch Bot Mac Address
  -c {TurnOn,TurnOff,Press,Down,Up}, --cmd {TurnOn,TurnOff,Press,Down,Up}
```
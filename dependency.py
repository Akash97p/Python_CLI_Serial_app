from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from pyfiglet import Figlet
import time
import argparse
import serial
import threading
from termcolor import colored, cprint   
from menus import *  
import serial.tools.list_ports as port_list
from serial_setup import *
import keyboard
import datetime
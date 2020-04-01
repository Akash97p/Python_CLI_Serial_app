from dependency import *
import keyboard
import datetime
global a
a ={}

def scan_ports():
    ports= list(port_list.comports())
    no_of_ports = len(ports)
    for i in range(no_of_ports):
        a[i] = ports[i].device
    print("  ","\U0001F449","Active Ports :")
    for i in range(no_of_ports):
        cprint ("     >",'white',end="", flush=True)
        cprint(a[i],'cyan')
    return a

def serial_open(vf):
    i = 1
    cnfg_file = open("config.json","r+")
    dic = eval((cnfg_file.read()))
    port = dic["port"]
    baud = dic["baud"]
    cnfg_file.close()
    ser = serial.Serial(port,baud)
    verbos_file = open("output.txt","w")
    verbos_file.write(str(datetime.datetime.now()))
    verbos_file.write("\n")
    verbos_file.close()
    verbos_file = open("output.txt","a")
    if ser.is_open == False:
        ser.open()
    while True:
        msg = str(ser.readline())
        if vf == 1:
            verbos_file.write(str_process(msg))
            verbos_file.write("\n")
        if (i%2) == 0:
            cprint(str_process(msg),'white')
        else:
            cprint(str_process(msg),'cyan')
            verbos_file.write(str_process(msg))
            verbos_file.write("\n")
        if keyboard.is_pressed('Esc'):
            break
        i = i+1


def str_process(msg):
    msg = msg.strip()
    msg = msg.replace("b'","")
    msg = msg.replace("\\r\\n'","")
    return msg
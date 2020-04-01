from dependency import *
import keyboard
import datetime
global a
a ={}
no_of_ports = 0

def scan_ports():
    global no_of_ports
    global a
    global port
    global pf
    port = ""
    a ={}
    b ={}
    pf = 1
    ports= list(port_list.comports())
    no_of_ports = len(ports)
    cnfg_file = open("config.json","r+")
    dic = eval((cnfg_file.read()))
    baud = dic["baud"]
    vf = dic["vf"]
    port = dic["port"]
    cnfg_file.close()
    for i in range(no_of_ports):
        a[i] = ports[i].device
    print("  ","\U0001F449","Active Ports :")
    for i in range(no_of_ports):
        cprint ("     >",'white',end="", flush=True)
        cprint(a[i],'cyan')
        if a[i] == port:
            c = port
        else:
            c = a[i]
    b["port"] = c
    b["baud"] = baud
    b["vf"] = vf
    cnfg_file = open("config.json","w")
    cnfg_file.write(str(b))
    cnfg_file.close()
    return a

def serial_open():
    if (len(scan_ports()) == 0):
        cprint("No ports available",'red')
        mm()
    else :
        i = 1
        cnfg_file = open("config.json","r+")
        dic = eval((cnfg_file.read()))
        port = dic["port"]
        baud = dic["baud"]
        vf = dic["vf"]
        cnfg_file.close()
        print("Connected to", port)
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
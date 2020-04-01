from dependency import *
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
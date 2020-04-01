from dependency import *
global a
a ={}
def scan_ports():
    ports= list(port_list.comports())
    no_of_ports = len(ports)
    for i in range(no_of_ports):
        a[i] = ports[i].device
    return a

# print("no of ports = ",no_of_ports,'green')
# for i in range(no_of_ports):
#     cprint(a[i],'cyan')
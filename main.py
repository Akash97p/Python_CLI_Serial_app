from ui import *

if platform.system() == 'Windows' :
    colorama.init()

if __name__ == "__main__":
    title_art('Serial CLI')
    while True:
        mm()

# b = scan_ports()
# for i in range(len(b)):
#     cprint(b[i],'cyan')

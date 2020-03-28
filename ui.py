from dependency import *
#from classes import *
f = Figlet(font='standard')

#---------------------------------------------------------------

global prev_baud
global prev_port
cnfg_file = open("config.json","r+")
dic = eval((cnfg_file.read()))
prev_port = dic["port"]
prev_baud = dic["baud"]
cnfg_file.close()
 
def prev_update():
    while True:
        global prev_baud
        global prev_port
        cnfg_file = open("config.json","r+")
        dic = eval((cnfg_file.read()))
        prev_port = dic["port"]
        prev_baud = dic["baud"]
        cnfg_file.close()
        time.sleep(1)

#----------------Titile ASCII Text with arts fonts--------------
def title_art(title):

    for i in range (30):
        cprint("-",'yellow', end="", flush=True)
        cprint("-",'blue', end="", flush=True)
    print("")
    cprint (f.renderText(title),'blue')
    for i in range (30):
        cprint("-",'yellow', end="", flush=True)
        cprint("-",'blue', end="", flush=True)
    print("")
    cprint("                  Welcom to Serial CLI tool",'yellow')
    for i in range (30):
        cprint("-",'yellow', end="", flush=True)
        cprint("-",'blue', end="", flush=True)
    print("")
    time.sleep(1)
#---------------------------------------------------------------

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#1E90FF',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#1E69FF bold',
    Token.Question: '',
})



def mm():
    # while True:
    global exit_flag
    global mm_sl
    mm_sl = prompt(main_menu,style=style)
    if mm_sl["menu_selec"] == 'Configuration':
        mm_sl.clear()
        conf_selec()
    elif mm_sl["menu_selec"] == 'Scan Ports':
        cprint("Sorry Function not implimented yet",'red')
        mm()
    elif mm_sl["menu_selec"] == 'Send data':
        cprint("Sorry Function not implimented yet",'red')
        mm()
    elif mm_sl["menu_selec"] == 'Open port':
        cprint("Sorry Function not implimented yet",'red')
        mm()
    else:
        exit_flag = True
        exit()
#--------------------------------------------------------------------------------------

def conf_selec():
    global prev_baud
    global prev_port
    global s_conf
    s_conf ={}
    cprint("Previus Conf  is : Port = {port} , Baud rate{baud}",'red'.format(port = prev_port , baud = prev_baud))
    prev_choice = prompt(prev_conf,style=style)
    if prev_choice["prev_continue"] == 'no':
        port = prompt(port_list, style=style)
        if port["port"] == 'Back':
            port.clear()
            mm()
        else:
            s_conf["port"] = port["port"]
            baud = prompt(baud_list, style=style)
            if baud["speed"] == 'Back':
                mm()
            elif baud["speed"] == 'Custom':
                baud.clear()
                cb = prompt(Custom, style=style)
                s_conf["baud"] = cb["Custom_Baud_rate"]
                cb.clear()
                cnfg_file = open("config.json","w")
                cnfg_file.write(str(s_conf))
                cnfg_file.close()
                mm()
                prev_port = s_conf["port"]
                prev_baud = s_conf["baud"]
            else:
                s_conf["baud"] = baud["speed"]
                baud.clear()
                cnfg_file = open("config.json","w")
                cnfg_file.write(str(s_conf))
                cnfg_file.close()
                mm()
                prev_port = s_conf["port"]
                prev_baud = s_conf["baud"]
    elif prev_choice["prev_continue"] == 'yes':
        pprint("Previus Configuration Selected")
        mm()
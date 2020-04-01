from dependency import *

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#06989a',  # default
    Token.Pointer: '#ffffff bold',
    Token.Instruction: '',  # default
    Token.Answer: '#1E69FF bold',
    Token.Question: '',
})

#---------------------------------------------------------------

def prev_update():
    global prev_baud
    global prev_port
    cnfg_file = open("config.json","r+")
    dic = eval((cnfg_file.read()))
    prev_port = dic["port"]
    prev_baud = dic["baud"]
    cnfg_file.close() 
    cprint("Previus Configuration  is :: Port : ",'cyan',end="", flush=True)
    cprint("{port}".format(port = prev_port),'red',end="", flush=True)
    cprint(" , Baud rate : ",'cyan',end="", flush=True)
    cprint("{baud}".format(baud = prev_baud),'red')
    cprint("Continue with Previus Configuration ?",'white')
    #time.sleep(1)

#----------------Titile ASCII Text with arts fonts--------------

def title_art(title):
    asc_title = "        " + title
    f = Figlet(font='standard')
    for i in range (30):
        cprint("-",'white', end="", flush=True)
        cprint("-",'cyan', end="", flush=True)
    print("")
    cprint (f.renderText(asc_title),'cyan')
    for i in range (30):
        cprint("-",'white', end="", flush=True)
        cprint("-",'cyan', end="", flush=True)
        time.sleep(.005)
    print("")
    cprint(":: {} ::".format(title),'white',end="", flush=True)
    cprint("                              Author : Akash",'cyan')
    cprint("                                              Version : 1.0",'cyan')
    for i in range (30):
        cprint("-",'white', end="", flush=True)
        cprint("-",'cyan', end="", flush=True)
        time.sleep(.005)
    print("")
    cprint("Use arrow keys to navigate , Enter to Select option",'white')

#---------------------------------------------------------------

def mm():
    # while True:
    global exit_flag
    global mm_sl
    mm_sl = prompt(main_menu,style=style)
    if mm_sl["menu_selec"] == '\U00002699  Configuration':
        mm_sl.clear()
        conf_selec()
    elif mm_sl["menu_selec"] == '\U0001F50D Scan Ports':
        mm_sl.clear()
        scan_ports()
    elif mm_sl["menu_selec"] == '\U0001F4E8 Send data':
        mm_sl.clear()
        cprint("Sorry Function not implimented yet",'red')
        mm()
    elif mm_sl["menu_selec"] == '\U0001F4E9 Open port':
        mm_sl.clear()
        serial_open()
    elif mm_sl["menu_selec"] == '\U0001F4D6 Help':
        mm_sl.clear()
        help()
    else:
        exit_flag = True
        exit()
#--------------------------------------------------------------------------------------

def conf_selec():
    global s_conf
    s_conf ={}
    prev_update()
    prev_choice = prompt(prev_conf,style=style)
    if prev_choice["prev_continue"] == 'no':
        port = prompt(ports_list, style=style)
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
            else:
                s_conf["baud"] = baud["speed"]
                baud.clear()
                cnfg_file = open("config.json","w")
                cnfg_file.write(str(s_conf))
                cnfg_file.close()
                mm()
    elif prev_choice["prev_continue"] == 'yes':
        cprint("Previus Configuration Selected",'green')
        mm()
from dependency import *

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#06989a',  # default
    Token.Pointer: '#ffffff bold',
    Token.Instruction: '',  # default
    Token.Answer: '#06989a',
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
    vf = dic["vf"]
    cnfg_file.close() 
    cprint("Current Config ::",'cyan',end="", flush=True)
    cprint(" Port : ",'white',end="", flush=True)
    cprint("{port}".format(port = prev_port),'red',end="", flush=True)
    cprint(" , Baud rate : ",'white',end="", flush=True)
    cprint("{baud}".format(baud = prev_baud),'red',end="", flush=True)
    cprint(" , Save output : ",'white',end="", flush=True)
    if vf == 1 :
        cprint("Yes",'green')
    else:
        cprint("No",'red')
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
    global verbos_flag
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
    global verbos_flag
    s_conf ={}
    prev_update()
    cprint("Continue with Current Configuration ?",'white', end="", flush=True)
    prev_choice = prompt(prev_conf,style=style)
    if prev_choice["prev_continue"] == 'No':
        cprint("Select Port : ",'white', end="", flush=True)
        port = prompt(ports_list, style=style)
        if port["port"] == 'Back':
            port.clear()
            mm()
        else:
            s_conf["port"] = port["port"]
            cprint("Select Speed : ",'white', end="", flush=True)
            baud = prompt(baud_list, style=style)
            if baud["speed"] == 'Back':
                mm()
            elif baud["speed"] == 'Custom':
                baud.clear()
                cprint("Enter custom baud rate :",'white', end="", flush=True)
                cb = prompt(Custom, style=style)
                s_conf["baud"] = cb["Custom_Baud_rate"]
                cb.clear()
                cnfg_file = open("config.json","w")
                cnfg_file.write(str(s_conf))
                cnfg_file.close()
                cprint("Save Serial monitor output to output.txt :",'white', end="", flush=True)
                sf = prompt(save, style=style)
                if sf["save_op"] == 'Yes':
                    s_conf["vf"] = 1
                    cnfg_file = open("config.json","w")
                    cnfg_file.write(str(s_conf))
                    cnfg_file.close()
                    mm()
                else :
                    s_conf["vf"] = 0
                    cnfg_file = open("config.json","w")
                    cnfg_file.write(str(s_conf))
                    cnfg_file.close()
                    mm()
            else:
                s_conf["baud"] = baud["speed"]
                baud.clear()
                cprint("Save Serial monitor output to output.txt :",'white', end="", flush=True)
                sf = prompt(save, style=style)
                if sf["save_op"] == 'Yes':
                    s_conf["vf"] = 1
                    cnfg_file = open("config.json","w")
                    cnfg_file.write(str(s_conf))
                    cnfg_file.close()
                    mm()
                else :
                    s_conf["vf"] = 0
                    cnfg_file = open("config.json","w")
                    cnfg_file.write(str(s_conf))
                    cnfg_file.close()
                    mm()
    elif prev_choice["prev_continue"] == 'Yes':
        #cprint("Previus Configuration Selected",'cyan')
        mm()
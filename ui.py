from dependency import *

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
    for i in range (60):
        print("-", end="", flush=True)
    print("")
    print (f.renderText(title))
    for i in range (60):
        print("-", end="", flush=True)
    print("")
    print("              Welcom to Serial CLI tool")
    for i in range (60):
        print("-", end="", flush=True)
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

#--------------------------------------------------------------------------------------

main_menu = [
    {
        'type': 'list',
        'message': '',
        'name': 'menu_selec',
        'choices': [
            {
                'name':'Scan Ports'
            },
            {
                'name':'Open port'
            },
            {
                'name':'Send data'
            },
            {
                'name':'Configuration'
            },
            {
                'name':'Exit'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 2 else True
    }
]

#--------------------------------------------------------------------------------------
prev_conf = [
    {
        'type': 'list',
        'message': 'Previus Conf  is : Port = {port} , Baud rate{baud}'.format(port = prev_port , baud = prev_baud),
        'name': 'prev_continue',
        'choices': [
            Separator('Continue with Previus Configuration'),
            {
                'name':'yes'
            },
            {
                'name':'no'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 2 else True
    }
]

#--------------------------------------------------------------------------------------

port_list = [
    {
        'type': 'list',
        'message': '',
        'name': 'port',
        'choices': [
            Separator('#  Available ports  #'),
            {
                'name':'ttyUSB0'
            },
            {
                'name':'ttyUSB1'
            },
            {
                'name':'ttyUSB2'
            },
                                    {
                'name': 'Back'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 2 else True
    }
]

#--------------------------------------------------------------------------------------

baud_list = [
    {
        'type': 'list',
        'message': 'Select Speed',
        'name': 'speed',
        'choices': [
            Separator('#  Baud Rate  #'),
            {
                'name': '300'
            },
            {
                'name': '1200'
            },
            {
                'name': '2400'
            },
            {
                'name': '4800'
            },
            {
                'name': '9600'
            },
            {
                'name': '19200'
            },
            {
                'name': '38400'
            },
            {
                'name': '57600'
            },
            {
                'name': '74880'
            },
            {
                'name': '115200',
                'checked': True
            },
            {
                'name': '230400'
            },
            {
                'name': '250000'
            },
                        {
                'name': '500000'
            },
                        {
                'name': '1000000'
            },
                        {
                'name': '2000000'
            },
                                    {
                'name': 'Custom'
            },
                                    {
                'name': 'Back'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 2 else True
    }
]

#--------------------------------------------------------------------------------------

Custom = [
    {
        'type': 'input',
        'name': 'Custom_Baud_rate',
        'message': 'Enter custom baud rate',
        'default': '9600'
    }
]

def mm():
    # while True:
    global exit_flag
    global mm_sl
    mm_sl = prompt(main_menu,style=style)
    if mm_sl["menu_selec"] == 'Configuration':
        mm_sl.clear()
        conf_selec()
    elif mm_sl["menu_selec"] == 'Scan Ports':
        print("Sorry Function not implimented yet")
        mm()
    elif mm_sl["menu_selec"] == 'Send data':
        print("Sorry Function not implimented yet")
        mm()
    elif mm_sl["menu_selec"] == 'Open port':
        print("Sorry Function not implimented yet")
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
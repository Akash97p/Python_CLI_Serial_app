from dependency import *
# List of Menu Structure

#---------------------------------------- Main Menu ---------------------------------------

main_menu = [
    {
        'type': 'list',
        'message': '',
        'name': 'menu_selec',
        'choices': [
            {
                'name':'\U00002699  Configuration'
            },
            {
                'name':'\U0001F50D Scan Ports'
            },
            {
                'name':'\U0001F4E9 Open port'
            },
            {
                'name':'\U0001F4E8 Send data'
            },
            {
                'name':'\U0001F4D6 Help'
            },
            {
                'name':'\U0000274E Exit'
            }
        ]
    }
]

#------------------------------ Select Previus Configuration ------------------------------

prev_conf = [
    {
        'type': 'list',
        'message': '',
        'name': 'prev_continue',
        'choices': [
            {
                'name':'yes'
            },
            {
                'name':'no'
            }
        ]
    }
]

#---------------------------------- Availavle Ports List- ---------------------------------

ports_list = [
    {
        'type': 'list',
        'message': '',
        'name': 'port',
        'choices': [
            {
                'name':'/dev/ttyUSB0'
            },
            {
                'name':'/dev/ttyUSB1'
            },
            {
                'name':'/dev/ttyUSB2'
            },
            {
                'name': 'Back'
            }
        ]
    }
]

#------------------------------------ Common Baud Rates ------------------------------------

baud_list = [
    {
        'type': 'list',
        'message': 'Select Speed',
        'name': 'speed',
        'choices': [
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
        ]
    }
]

#------------------------------------- Custome_baudRate ------------------------------------

Custom = [
    {
        'type': 'input',
        'name': 'Custom_Baud_rate',
        'message': 'Enter custom baud rate',
        'default': '9600'
    }
]

#---------------------------------------------------------------------------------------

def help():
    cprint("\U0001F4A1 Use arrow keys to navigate.",'green')
    cprint("\U0001F4A1 Press Enter to Select option.",'yellow')
    cprint("\U0001F4A1 Long Press",'green',end="", flush=True)
    cprint(" Esc ",'red',end="", flush=True)
    cprint("to exit from serial monitor",'green')
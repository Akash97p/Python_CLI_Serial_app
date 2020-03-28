# List of Menu Structure

#---------------------------------------- Main Menu ---------------------------------------

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

port_list = [
    {
        'type': 'list',
        'message': '',
        'name': 'port',
        'choices': [
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
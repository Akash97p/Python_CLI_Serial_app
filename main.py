from dependency import *
global exit_flag
exit_flag = False
#----------------Titile ASCII Text with arts fonts--------------

title_art('Serial CLI')

#-------------------------main_menu-----------------------------

#------------------------Config_Selection-----------------------

#---------------------------Serial_Listener---------------------

# main Threads
menu = threading.Thread(target=mm)
update_config = threading.Thread(target=prev_update)
menu.start()
update_config.start()

while exit_flag :
    menu.stop()
    update_config.stop()
    exit()


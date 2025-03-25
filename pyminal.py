import os
import cmd
import sys
import datetime
import time

dir = "home/"
version = "0.0.1"

#opperations begin here
print(f"""                       _             _   
 _ __  _   _ _ __ ___ (_)_ __   __ _| |            
| '_ \| | | | '_ ` _ \| | '_ \ / _` | |            
| |_) | |_| | | | | | | | | | | (_| | |            
| .__/ \__, |_| |_| |_|_|_| |_|\__,_|_|            
|_|    |___/                                       
                                                   
version, {version}                                 
the python based terminal                          
made by minty2                                     
                                                   
for first time users type 'initialize'             
for help type 'help'                               
for a list of installed packages type 'pkgs'       
remember to never run anything from an untrested   
source                                             
                                                   
you should be able to see the cursor below         
adjust in order to the the cursor                  
___________________________________________________
""")

class Pyminnal(cmd.Cmd):
    prompt = 'dir'
    file = None
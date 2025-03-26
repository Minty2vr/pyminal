import cmd
import datetime
import time
import subprocess
#thats a lot of imports O.O

dir = "home/"
version = "0.1.0"

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
                                                   
for help type 'help'                               
       
for first time users type 'tutorial'


                                                   
you should be able to see the cursor below         
adjust in order to the the cursor                  
___________________________________________________
""")

class Pyminnal(cmd.Cmd):
    prompt = dir
    file = None

    def do_hello(self, line):
        '''tests the print function and make sures things workey'''
        print("Hello, World!") #prints 'Hello, World!' as a test

    def do_help(self, arg):
        '''lists commmands and what they do'''
        return super().do_help(arg)

    def do_quit(self, line):
        '''closes pyminal'''
        return True #exits Py-Cal
    
    def do_today(self, line):
        '''prints todays date'''
        now = datetime.datetime.now()
        print(now.strftime('today is %A, %B %d %Y, %I:%M%p'))

    def do_open(self, fileToRun):
        '''runs the specified file. case sensitive. 
only opens files in the "pyminal" folder'''
        subprocess.run(["python", fileToRun])

    def do_tutorial(self, line):
        '''opens the tutorial file that came with pyminal'''
        subprocess.run(["python", "tutorial.py"])

if __name__ == '__main__':
    Pyminnal().cmdloop()

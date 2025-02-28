import os

dir = "home/"
version = "0.0.1"

#opperations begin here
print(f"""                       _             _   
 _ __  _   _ _ __ ___ (_)_ __   __ _| |           
| '_ \| | | | '_ ` _ \| | '_ \ / _` | |            
| |_) | |_| | | | | | | | | | | (_| | |            
| .__/ \__, |_| |_| |_|_|_| |_|\__,_|_|            
|_|    |___/                                       
                                                   
the python based terminal                          
made by minty2                                     
                                                   
version, {version}                                 
for first time users type 'initialize'             
for help type 'help'                               
for a list of installed packages type 'pkgs'       
remember to never run anything from an untrested   
source                                             
                                                   
you should be able to see the cursor below         
adjust in order to the the cursor                  
___________________________________________________
""")
while True: 
    userInput = input(dir)
    
    if userInput.lower() == 'initialize': #the function for making the file that has the list of commands
        print("")
        print("please wait while pyminal gets set up...")
        
        with open ('pyminal_packages.txt', 'w+') as file:
            print("package handling created")
        
        print("")
        print("Hello!")
        print("""Welcome to pyminal.
this is a termial built entirely within python.
to navigate type where you want to go! for example
if you have a calculator package hooked type
'calculator' in the home directory

for more info or you just need help type 'help' in
the home directory. or visit 
'https://github.com/Minty2vr/pyminal' 
""")
    elif userInput.lower() == 'clear':
         os.system('cls' if os.name == 'nt' else 'clear')

    elif userInput.lower() == 'help':
        print("""for help about pyminal visit 
'https://github.com/Minty2vr/pyminal'""")
        print("commands")
        with open ('pyminal_packages.txt', 'r') as file:
            print(file.readline())


    else:
        print(f"Error 01: {userInput} not a command")
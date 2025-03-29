import cmd,subprocess

#hey!
#for info on making your own packages for pyminal
#check out the github repo or follow the tutorial

#the tutorial teaches you about how to use pyminal
#and other cool things like making packages and
#some basic guidlines to follow when making
#your own packages

#i am not responsible for packages that may contain
#malware. i do understand how easy it is to uplaod
#malware and to prevent that i test packages myself
#see the safe packages list for malware free packages
#to play around with

version = '0.0.1'

print('pyminal tutorial version', version)
print()

print("""Hello! welcome to the pyminal tutorial!
the goal here is to get you ready to create and use
your own files like this one!
(enter to continue)""")

input()

print("""
first things first. you will need to know how to 
navigate pyminal. if you noticed before you got
here you started in "home/" home is where you
start your day. and its also where pyminal starts
its day
(enter to continue)""")

input()

print("""
pyminal works on a home/argument/detail basis.
its keeps things simple. you got here by typing an
argument. arguments tell pyminal what you want the
program to do. and the details tell pyminal how.
for example. to run a file, type 'open' then the 
program name. the open command is the argument and
the details are which file to open.""")

input('(press enter to continue)')
print()

print('''how to make your own package
      
this is really simple. all you need is a way to 
get back pyminal and you're set! packages run on
python, just like this tutorial. to get back to
pyminal use the subprocess module. the code should
look something like the following''')
print() #empty line
print('''import subprocess

input('would you like to exit the program? y/n')
    if input == 'y':
        subprocess.run(["python", "pyminal.py"])
''')

input("(press enter to exit the tutorial)")
subprocess.run(["python", "pyminal.py"])
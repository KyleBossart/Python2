#!/usr/bin/env python
# Above shebang used to point to which program to run it as. Have to give the script executable permissions with "chmod +x ban.py". Has to be on Line 1 to work.


# December 15, 2020

# A simple python script that allows user to change Bandit level by running instead of having to manually change the Bandit level each time. Now instead of holding back arrow for 3 seconds and hitting three keys, I can type out a command. yay.
#-----------------------------------------------------------------------------------------------------------------------------------------------

# Imports "os" which allows ban.py to use the os.system command below to output the text into bash.
import os

# Asking the user which Bandit level they want to SSH into and putting their answer into the "num" variable.
num = input("Which Bandit level would you like to access?")

# "bannum" (short for bandit number) is a variable that stores the first part of the string, appends the "num" variable, and then appends the second part of the string.
bannum = ("ssh bandit" + num + "@bandit.labs.overthewire.org -p 2220")

# os.system takes the "bannum" variable and outputs it into a shell command. Reduntant comment :).
os.system(bannum)

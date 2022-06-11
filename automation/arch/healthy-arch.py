#!/usr/bin/env python3

from subprocess import Popen, PIPE

class Utility:
    def __init__(self, description, commands):
        self.description = description
        self.commands = commands

    # def execute(self):
        # run_command(self.command)

class Command:
    def __init__(self, command):
        self.command = command

    def run(self):
        try:
            process = Popen(command, text=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
            print(out)
        except:
            print("There was an error, please try again.")

class Menu:
    def __init__(self, items):
        self.items = items

    def show(self):
        # PRINT ALL THE ITEMS
        option = int(input("Please select an OPTION: "))


def main():
    Menu([
        Utility('0 - System Information.', ["neofetch"]), 
        Utility('1 - System Upgrade.', ["sudo pacman -Syu"]),
        Utility('2 - Exit.', ["exit"])
        ]).show()

# Start the script
while (True):
    main()
#!/usr/bin/env python3

import shutil
from subprocess import Popen, PIPE

class Utility:
    def __init__(self, description, command):
        self._description = description
        self._command = command

    @property
    def description(self):
        return self._description

    def execute(self):
        Command(self._command).run()

class Command:
    def __init__(self, command):
        self._command = shutil.which(command)

    def run(self):
        try:
            # https://docs.python.org/3/library/subprocess.html
            process = Popen(self._command, text=True, stdout=PIPE, stderr=PIPE)
            out, err = process.communicate()
            print(out)
        except:
            print("There was an error!!! Please try again ;).")

class Menu:
    def __init__(self, items):
        self._items = items

    def show(self):
        self.print_header()
        self.print_items()
        self.print_footer()
        self.wait_for_option()

    def print_header(self):
        print('----------------------------')
        print('  Healthy Arch Linux 1.0.0  ')
        print('----------------------------')

    def print_items(self):
        for item in self._items:
            print(item.description)

    def print_footer(self):
        print('----------------------------')

    def wait_for_option(self):
        option = int(input("Please select an OPTION: "))
        self._items[option].execute()

def main():
    Menu([
        Utility('0 - System Information.', "neofetch"), 
        Utility('1 - System Upgrade.', "sudo pacman -Syu"),
        Utility('2 - Exit.', "exit 0")
        ]).show()

# Start the script
while (True):
    main()
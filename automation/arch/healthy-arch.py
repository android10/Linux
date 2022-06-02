#!/usr/bin/env python3

class Utility:
    def __init__(self, description, command):
        self.description = description
        self.command = command

    def run(self):
        return self.command

class Menu:
    def __init__(self, items):
        self.items = items

    def show(self):
        print('TODO MENU: make it nice and colourful')
        print('SELECT AN OPTION: ')

def main():
    menu = Menu([
        Utility('0 - System Information.', 'neofetch'), 
        Utility('1 - System Upgrade.', 'sudo pacman -Syu')]
        ).show()

# Start the script
main()
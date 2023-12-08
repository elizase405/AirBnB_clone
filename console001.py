#!/usr/bin/python3

"""
Title: Command interpreter
Description: for debugging and development (front-end use here)
Authors: Elizabeth Akindele & Idoko Attah
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class definition """

    prompt = "(hbnb)"  # custom prompt given

    # implementing the quit, EOF, and help commands
    def do_quit(self, args):
        """
        cmd method for quitting the program
        """
        return True

    def do_EOF(self, args):
        """
        cmd method for exiting the program
        """
        # print()  # print an empty line
        return True

    def help_quit(self):
        """
        cmd help method
        """
        print("Quit command to exit the program")
        print()  # prints an empty line


if __name__ == '__main__':
    HBNBCommand().cmdloop()

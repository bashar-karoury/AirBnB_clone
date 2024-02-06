#!/usr/bin/python3
"""
    Command Interpreter to manipulate data without a visual interface
    and as entry point of project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command Processor inhereited from Cmd class to enable manipulating
        data without visual interface
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ handler of EOF marker to exit the processor cleanly

            Args:
                line: read line from stdin

            Return:
                (boolean): status of code of executing the processor
        """
        return True

    def help_EOF(self):
        """ print help message for EOF command
        """
        print("EOF command to exit the program")

    def do_quit(self, line):
        """ handler of quit command to exit the processor cleanly

            Args:
                line: read line from stdin

            Return:
                (boolean): status of code of executing the processor
        """
        return True

    def help_quit(self):
        """ print help message for quit command
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """ handle an empty line command
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

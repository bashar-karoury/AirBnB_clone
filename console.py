#!/usr/bin/python3
"""
    Command Interpreter to manipulate data without a visual interface
    and as entry point of project
"""
import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, line):
        """ creates a new instance of BaseModel object

            Args:
                line (str): read line from stdin, should have one arg
                            as the class name of BaseModel object
        """
        # tokenize read line
        args = line.split()
        if not args[0]:
            print("** class name missing **")
            return
        if not isinstance(args[0], BaseModel):
            print("** class doesn't exist **")
            return
        # get class from classname
        BaseModelClass = getattr(__main__, args[0])
        obj = BaseModelClass()
        # save it to storage
        storage.new(obj)
        storage.save()
        # print id
        print(obj.id)

    def help_create(self):
        """ print help message of create command
        """
        print("Create command to create new instance of BaseModle object")
        print("Usage:")
        print("create [Classname]")

    def do_show(self, line):
        """ prints BaseModel object with specific id

            Args:
                line (str): read line from stdin, should have two args
                            class name and id of object
        """
        # tokenize read line
        args = line.split()

        # check class name
        if not args[0]:
            print("** class name missing **")
            return
        if not isinstance(args[0], BaseModel):
            print("** class doesn't exist **")
            return

        # check id
        if not args[1]:
            print("** instance id missing **")
            return
        # get all dictionary
        all_objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key in all_objs:
            print(all_obj[obj_key])
        else:
            print("** no instance found **")

    def help_show(self):
        """ print help message of show command
        """
        print("Show command to prints an instance with id")
        print("Usage:")
        print("show [Classname] [id]")

    def do_all(self, line):
        """ prints all objects based or not on class name

            Args:
                line (str): read line from stdin, may be empty or have one arg
                            as class name
        """
        # tokenize read line
        args = line.split()

        # check class name if found
        if not args[0]:
            if not isinstance(args[0], BaseModel):
                print("** class doesn't exist **")
                return
        # get all dictionary
        all_objs = storage.all()
        if args[0]:
            # there is class name provided
            print([all_objs[k] for k in all_objs if args[0] + "." in k])
        else:
            print(list(all_objs.values()))

    def help_all(self):
        """ Prints all string representation of all instances based
            or not on the class name
        """
        print("all command to all objects of class if provided")
        print("Usage:")
        print("all [Classname]")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

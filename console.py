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
        # save it to dictionary of objects
        storage.new(obj)

        # save changes to file
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

    def do_update(self, line):
        """ Update attribute of object of class with specific id

            Args:
                line (str): read line from stdin, should have four args
                            class name, id, attribute name, attribute value
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

        # check id presence
        if not args[1]:
            print("** instance id missing **")
            return
        # get all dictionary
        all_objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        # get object reference
        obj = all_objs[obj_key]

        # check attribute name presence
        if not args[2]:
            print("** attribute name missing **")
            return

        # check attribute value presence
        if not args[3]:
            print("** value missing **")
            return

        # set attribute with given value
        setattr(obj, args[2], args[3])

        # save changes to file
        storage.save()

    def help_update(self):
        """ print help message of update command
        """
        print("Update command to update or set attribute of object")
        print("Usage:")
        print("update [Classname] [id] [attribute name] [attribute value]")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id

            Args:
                line (str): read line from stdin, should have two args
                            class name and id
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

        # check id presence
        if not args[1]:
            print("** instance id missing **")
            return
        # get all dictionary
        all_objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        # delete object
        del all_objs[obj_key]

        # save changes to file
        storage.save()

    def help_destroy(self):
        """ print help message of destroy command
        """
        print("Destroy command to delete object")
        print("Usage:")
        print("destroy [Classname] [id]")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

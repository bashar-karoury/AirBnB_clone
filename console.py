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
        # check class name
        if not args:
            print("** class name missing **")
            return
        # check if first arg represent a valid class
        try:
            if not isinstance(eval(args[0] + "()"), BaseModel):
                print("** class doesn't exist **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

        obj = eval(args[0] + "()")
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
        if not args:
            print("** class name missing **")
            return
        # check if first arg represent a valid class
        try:
            if not isinstance(eval(args[0] + "()"), BaseModel):
                print("** class doesn't exist **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

        # check id
        if len(args) < 2:
            print("** instance id missing **")
            return
        # get all dictionary
        all_objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key in all_objs:
            print(all_objs[obj_key])
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
        # check class name
        if args:
            # check if first arg represent a valid class
            try:
                if not isinstance(eval(args[0] + "()"), BaseModel):
                    print("** class doesn't exist **")
                    return
            except NameError:
                print("** class doesn't exist **")
                return
        # get all dictionary
        all_objs = storage.all()
        if args:
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
        if not args:
            print("** class name missing **")
            return
        try:
            if not isinstance(eval(args[0] + "()"), BaseModel):
                print("** class doesn't exist **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

        # check id presence
        if len(args) < 2:
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
        if len(args) < 3:
            print("** attribute name missing **")
            return

        # check attribute value presence
        if len(args) < 4:
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
        if not args:
            print("** class name missing **")
            return
        try:
            if not isinstance(eval(args[0] + "()"), BaseModel):
                print("** class doesn't exist **")
                return
        except NameError:
            print("** class doesn't exist **")
            return

        # check id presence
        if len(args) < 2:
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

    
    def default(self, line):
        """ handler of other Commands

            Args:
                line (str): input from user
        """
        # parse line into '.' separeted words
        args = line.split('.')
        if len(args) != 2:
            print("*** Unknown syntax: {}".format(line))
            return
        Class_name, call_line = args
        # validate class name
        try:
            if not isinstance(eval(Class_name + "()"), BaseModel):
                print("** class doesn't exist **")
                return
        except NameError:
            print("** class doesn't exist **")
            return
        # validate call
        # strip call from arguments
        call, args_list = HBNBCommand.extract_call_and_args(call_line)
        print(call)
        print(args_list) 
        print("Yaaaaaaaay")

    
    @staticmethod
    def extract_call_and_args(call_line):
        """ static method to extract call and argumetns out of Class
            based commands

            Args:
                call_line (str): call line after the '.'
        
            Return:
                tuple: contains the call and list of arguments to the call
        """
        i = call_line.find("(")
        if i == -1:
            return (None, None)
        call = call_line[:i]
        args = call_line[i + 1:].strip(")")
        args_list = [arg.strip() for arg in args.split(",")]
        return (call, args_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()


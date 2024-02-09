#!/usr/bin/python3
"""
    Command Interpreter to manipulate data without a visual interface
    and as entry point of project
"""
import cmd
from models import storage
from models.base_model import BaseModel
import re
import json
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
        class_name = args[0]
        try:
            if (class_name not in globals() 
            or not issubclass(globals()[class_name], BaseModel)):
                print("** class doesn't exist **")
                return
        except Exception:
            print("** class doesn't exist **")
            return
        cls = globals()[class_name]
        obj = cls()
        # relaod from file
        storage.reload()

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
        class_name = args[0]
        try:
            if (class_name not in globals()
            or not issubclass(globals()[class_name], BaseModel)):
                print("** class doesn't exist **")
                return
        except Exception:
            print("** class doesn't exist **")
            return

        # check id
        if len(args) < 2:
            print("** instance id missing **")
            return
        # reload first
        storage.reload()

        # get all dictionary
        all_objs = storage.all()
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
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
            class_name = args[0]
            try:
                if (class_name not in globals()
                or not issubclass(globals()[class_name], BaseModel)):
                    print("** class doesn't exist **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        # reload from file
        storage.reload()

        # get all dictionary
        all_objs = storage.all()
        if args:
            # there is class name provided
            
            print([str(all_objs[k]) for k in all_objs if class_name + "." in k])
        else:
            print([str(all_objs[k]) for k in all_objs])

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

        # check if first arg represent a valid class
        if not args:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        try:
            if (class_name not in globals()
            or not issubclass(globals()[class_name], BaseModel)):
                print("** class doesn't exist **")
                return
        except Exception:
            print("** class doesn't exist **")
            return

        # check id presence
        if len(args) < 2:
            print("** instance id missing **")
            return
        # reload from file
        storage.reload()

        # get all dictionary
        all_objs = storage.all()
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
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
        att_name = args[2]
        att_value
        setattr(obj, att_name, att_value)

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
        # check if first arg represent a valid class
        if not args:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        try:
            if (class_name not in globals()
            or not issubclass(globals()[class_name], BaseModel)):
                print("** class doesn't exist **")
                return
        except Exception:
            print("** class doesn't exist **")
            return

        # check id presence
        if len(args) < 2:
            print("** instance id missing **")
            return
        # reload from file
        storage.reload()

        # get all dictionary
        all_objs = storage.all()
        obj_id = args[1]
        obj_key = class_name + "." + obj_id
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
        class_name, call_line = args
        # validate class name
        try:
            if (class_name not in globals()
            or not issubclass(globals()[class_name], BaseModel)):
                print("** class doesn't exist **")
                return
        except Exception:
            print("** class doesn't exist **")
            return

        # validate call
        # strip call from arguments
        call, args_list = HBNBCommand.extract_call_and_args(call_line)
        print(call)
        print(args_list)
        
        # check call
        if call == "all":
            HBNBCommand.all(class_name)
        elif call == "count":
            HBNBCommand.count(class_name)
        elif call == "show":
            HBNBCommand.show(class_name, args_list)
        elif call == "create":
            HBNBCommand.create(class_name)
        elif call == "destroy":
            HBNBCommand.destroy(class_name, args_list)
        elif call == "update":
            HBNBCommand.update(class_name, args_list)
        else:
            print("undefined call")

    @staticmethod    
    def all(class_name):
        """ helper function to list all objects of specific class
            
            Args:
                class_name (str): name of class
        """
        # reload from file 
        storage.reload()

        # get all dictionary
        all_objs = storage.all()

        # there is class name provided
        print([str(all_objs[k]) for k in all_objs if class_name + "." in k])
 
    @staticmethod    
    def count(class_name):
        """ helper function to count all objects of specific class
            
            Args:
                class_name (str): name of class
        """
        # reload from file 
        storage.reload()

        # get all dictionary
        all_objs = storage.all()

        # there is class name provided
        print(len([all_objs[k] for k in all_objs if class_name + "." in k]))
 

    @staticmethod    
    def create(class_name):
        """ helper function to list all objects of specific class
            
            Args:
                class_name (str): name of class
        """
        # reload from file 
        storage.reload()

        obj = globals()[class_name]()
        # save it to dictionary of objects
        storage.new(obj)

        # save changes to file
        storage.save()

        # print id
        print(obj.id) 

    @staticmethod    
    def show(class_name, args_list):
        """ helper function to print object with specific id
            
            Args:
                class_name (str): name of class
                args_list (list): list of arguments provided to show
        """
        # check id
        if len(args_list) < 1:
            print("** instance id missing **")
            return
        # reload from file 
        storage.reload()
       # get all dictionary
        all_objs = storage.all()
        obj_id = args_list[0]
        # strip '"' out of id
        obj_id = args_list[0].replace('"','')

        obj_key = class_name + "." + obj_id
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")   
  
    @staticmethod    
    def destroy(class_name, args_list):
        """ helper function to destroy object with specific id
            
            Args:
                class_name (str): name of class
                args_list (list): list of arguments provided to show
        """
       # check id presence
        if len(args_list) < 1:
            print("** instance id missing **")
            return
        # reload from file 
        storage.reload()

        # get all dictionary
        all_objs = storage.all()
        obj_id = args_list[0]
        # strip '"' out of id
        obj_id = args_list[0].replace('"','')

        obj_key = class_name + "." + obj_id
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        # delete object
        del all_objs[obj_key]

        # save changes to file
        storage.save()        
 
    @staticmethod    
    def update(class_name, args_list):
        """ helper function to update object with specific id
            
            Args:
                class_name (str): name of class
                args_list (list): list of arguments provided to update
        """
        # check id presence
        if len(args_list) < 1:
            print("** instance id missing **")
            return
        # strip quotation marks from id
        # args_list[0].replace('"','')
        # reload to update dict of objects
        storage.reload()
        # get all dictionary
        all_objs = storage.all()
        # strip '"' out of id
        obj_id = args_list[0].replace('"','')
        obj_key = class_name + "." + obj_id
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        # get object reference
        obj = all_objs[obj_key]
        
        # check attribute name presence
        if len(args_list) < 2:
            print("** attribute name missing, No dictionary is found **")
            return
        # check if second arg is dictionary
        if type(eval(args_list[1])) == dict:
            attr_dict = eval(args_list[1])
            for key, value in attr_dict.items():
                print("{}:{}".format(key, value))
                setattr(obj, key, value)
        else:
            # check attribute value presence
            if len(args_list) < 3:
                print("** value missing **")
                return
            # set attribute with given value
            # attr_name = args_list[1].replace('"','')
            # attr_value = args_list[2].replace('"','')
            attr_name = eval(args_list[1])
            attr_value = eval(args_list[2])
            setattr(obj, attr_name, attr_value)

        # save changes to file
        storage.save()

                       
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
        """
        args_list = [arg.strip() for arg in args.split(",")]
        # arguments may be passed with quotation marks, they should be striped
        for i in range(len(args_list)):
            args_list[i] = args_list[i].replace('"', '')
        """
        pattern = r'[^,{}]+|{[^{}]+}'
        args = args.replace(" ","")
        args_list = re.findall(pattern, args)
        # strip leading whitspaces and quotation marks if found
        for i in range(len(args_list)):
            args_list[i] = args_list[i].strip()
        return (call, args_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()


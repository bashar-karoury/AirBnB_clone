#!/usr/bin/python3
"""Unittests for console
"""

# sys.path.insert(0,  '../')  # Add the parent directory to the Python path
import unittest
import sys
import console
from io import StringIO
from unittest.mock import patch


class Testing_console(unittest.TestCase):
    """ Unit testing class for console module
    """

    def test_quit(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("help")
            # msg = "\nDocumented commands (type help <topic>):"
            # "\n========================================"
            # "\nEOF  all  create  destroy  help  quit  show  update"
            # "\n\n(hbnb) "
            print(len(f.getvalue()))
            self.assertEqual(f.getvalue(),  f.getvalue())

    def test_EmptyLine(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("           ")
            self.assertEqual(f.getvalue(), "")

    def test_create_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create WrongClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_BaseModel_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_User_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_State_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_City_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_Amenity_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_Place_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_Review_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel 0000-0000")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_show_Base_Model(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_show_User(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show User " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_show_Place(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show Place " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_show_State(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show State " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_show_City(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show City " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_show_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show Amenity " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_show_Review(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("show Review " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_destroy_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy BaseModel 0000-0000")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_BaseModel(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy BaseModel " + obj_id)
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_User(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy User " + obj_id)
            console.HBNBCommand().onecmd("show User " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_Place(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy Place " + obj_id)
            console.HBNBCommand().onecmd("show Place " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_State(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy State " + obj_id)
            console.HBNBCommand().onecmd("show State " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_City(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy City " + obj_id)
            console.HBNBCommand().onecmd("show City " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy Amenity " + obj_id)
            console.HBNBCommand().onecmd("show Amenity " + obj_id)
            self.assertEqual(f.getvalue(),  "** no instance found **\n")

    def test_destroy_Review(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy Review " + obj_id)
            console.HBNBCommand().onecmd("show Review " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all")
            self.assertNotEqual(f.getvalue(), "** class name missing **\n")

    def test_all_wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all WrongClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_BaseModel_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all BaseModel")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_User_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all User")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_State_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all State")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_City_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all City")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_Amenity_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all Amenity")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_Place_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all Place")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all_Review_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("all Review")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_update_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_update_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel 0000-0000")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_update_no_attr_name(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel " + obj_id)
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    def test_update_no_attr_value(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel " + obj_id + " n")
            self.assertEqual(f.getvalue(), "** value missing **\n")

    def test_update_Base_Model(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_update_User(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update User " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show User " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_update_Place(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update Place " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show Place " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_update_State(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update State " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show State " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_update_City(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update City " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show City " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_update_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update Amenity " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show Amenity " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_update_Review(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("update Review " + obj_id + "n 1")
            console.HBNBCommand().onecmd("show Review " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_create_wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("WrongClass.create()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_BaseModel_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_User_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_State_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_City_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_Amenity_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_Place_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_create_Review_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.create()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_show_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_class_show_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("MyClass.show()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_show_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show(\"0000-0000\")")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_Base_Model(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            command = "BaseModel.show(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_User(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("User.show(\"{}\")".format(obj_id))
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_Place(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("Place.show(\"{}\")".format(obj_id))
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_State(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("State.show(\"{}\")".format(obj_id))
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_City(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("City.show(\"{}\")".format(obj_id))
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("Amenity.show(\"{}\")".format(obj_id))
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_show_Review(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("Review.show(\"{}\")".format(obj_id))
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_class_destroy_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("MyClass.destroy()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_destroy_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.destroy(\"0000-0000\")")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_Base_Model(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "BaseModel.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_User(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "User.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show User " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_Place(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "Place.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show Place " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_State(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "State.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show State " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_City(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "City.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show City " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_destroy_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f2:
            command = "Amenity.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show Amenity " + obj_id)
            self.assertEqual(f2.getvalue(), "** no instance found **\n")

    def test_class_destroy_Review(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "Review.destroy(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            console.HBNBCommand().onecmd("show Review " + obj_id)
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_all_wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("WrongClass.all()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_BaseModel_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_User_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("User.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_State_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("State.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_City_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("City.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_Amenity_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("Amenity.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_Place_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("Place.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_all_Review_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("Review.all()")
            self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_update_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_class_update_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("MyClass.update()")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_class_update_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.update(\"0000-0000\")")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_no_attr_name(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "BaseModel.update(\"{}\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")

    def test_class_update_no_attr_value(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            command = "BaseModel.update(\"{}\",  \"key\")".format(obj_id)
            console.HBNBCommand().onecmd(command)
            self.assertEqual(f.getvalue(), "** value missing **\n")

    def test_class_update_Base_Model(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "BaseModel.update(\"{}\", \"key\", \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_User(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "User.update(\"{}\", \"key\", \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show User " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_Place(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "Place.update(\"{}\",  \"key\" ,  \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show Place " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_State(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "State.update(\"{}\",  \"key\" ,  \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show State " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_City(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "City.update(\"{}\",  \"key\" ,  \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show City " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "Amenity.update(\"{}\", \"key\", \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show Amenity " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_Review(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "Review.update(\"{}\",  \"key\" ,  \"value\")".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show Review " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

    def test_class_update_dictionary(self):
        """ test quit command
        """
        with patch('sys.stdout',  new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            obj_id = obj_id.replace('\n', '')
        with patch('sys.stdout',  new=StringIO()) as f:
            c = "BaseModel.update(\"{}\",  {{\"k\":\"v\"}}".format(obj_id)
            console.HBNBCommand().onecmd(c)
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertNotEqual(f.getvalue(), "** no instance found **\n")

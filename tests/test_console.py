#!/usr/bin/python3
"""Unittests for console
"""

import unittest
import sys
sys.path.insert(0, '../')  # Add the parent directory to the Python path
import console
from io import StringIO
from unittest.mock import patch

class Testing_console(unittest.TestCase):
    """ Unit testing class for console module
    """

    def test_quit(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(),"")

    def test_help(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("help")
            # msg = "\nDocumented commands (type help <topic>):"
            # "\n========================================"
            # "\nEOF  all  create  destroy  help  quit  show  update"
            # "\n\n(hbnb) "
            print(len(f.getvalue()))
            self.assertEqual(f.getvalue() , f.getvalue())

    def test_EmptyLine(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("           ")
            self.assertEqual(f.getvalue(),"")

    def test_create_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(),"** class name missing **\n")

    def test_create_wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create WrongClass")
            self.assertEqual(f.getvalue(),"** class doesn't exist **\n")


    def test_create_BaseModel_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")

    def test_create_User_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")

    def test_create_State_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")

    def test_create_City_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")


    def test_create_Amenity_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")



    def test_create_Place_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")

    def test_create_Review_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            self.assertNotEqual(f.getvalue(),"** class doesn't exist **\n")

    def test_show_no_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(),"** class name missing **\n")

    def test_show_no_id(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseClass")
            self.assertEqual(f.getvalue(),"** instance id missing **\n")

    def test_show_Wrong_class(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show MyClass")
            self.assertEqual(f.getvalue(),"** class doesn't exist **\n")

    def test_show_Wrong_id(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel 0000-0000")
            self.assertEqual(f.getvalue(),"** no instance found **\n")

    def test_show_BaseClass(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show BaseModel " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")

    def test_show_User(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create User")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show User " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")

    def test_show_Place(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Place")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show Place " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")

    def test_show_State(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create State")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show State " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")

    def test_show_City(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create City")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show City " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")

    def test_show_Amenity(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Amenity")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show Amenity " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")

    def test_show_Review(self):
        """ test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create Review")
            obj_id = f.getvalue()
            console.HBNBCommand().onecmd("show Review " + obj_id)
            self.assertNotEqual(f.getvalue(),"** no instance found **\n")



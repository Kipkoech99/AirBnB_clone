#!/usr/bin/python3
"""module for command line interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
        This is the entry point to our program
    """

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Checks for End of File"""
        print ()
        return True

    def do_quit(self, args):
        """Handles quit command"""
        return True

    def emptyline(self):
        """Handles ENTER press"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if args == "" or args is None:
            print("** class name missing **")
        elif args not in storage.classes():
            print("** class doesn't exist **")
        else:
            ob = storage.classes()[args]()
            ob.save()
            print(ob.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name and id"""
        if args == "" or None:
            print("** class name missing **")
        else:
            token = args.split(' ')
            if token[0] not in storage.classes():
                print("** class doesn't exist **")
            elif token[1] == "" or None:
                print("** instance id missing **")
            else:
                key = f"{token[0]}.{token[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


if __name__=="__main__":
    HBNBCommand().cmdloop()

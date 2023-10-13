#!/usr/bin/python3
"""module for command line interpreter"""
import sys
import cmd
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
        if args == "" or args is None:
            print("** class name missing **")
        else:
            token = args.split(' ')
            if token[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(token) < 2 or token[1] is None:
                print("** instance id missing **")
            else:
                key = f"{token[0]}.{token[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if args == "" or args is None:
            print("** class name missing **")
        else:
            word = args.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = f"{word[0]}.{word[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
    
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        if args:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                instances = storage.all()
                class_instances = []
                for key, value in instances.items():
                    if key == class_name:
                        class_instances = [str(instance) for instance in class_name]
                return class_instances
        else:
            instance_list = [str(instance) for instance in storage.all().values()]
            print(instance_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        if args == "" or args is None:
            print("** class name missing **")
        else:
            word = args.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            elif len(word) < 3:
                print("** attribute name missing **")
            elif len(word) < 4:
                print("** value missing **")
            else:
                key = f"{word[0]}.{word[1]}"
                instances = storage.all()
                if key in instances:
                    instance = instances[key]
                    setattr(instance, word[2], word[3].strip('"'))
                    storage.save()
                else:
                    print("** no instance found **")

    def do_test(self, args):
        classes = storage.classes()
        print(classes)

        


if __name__=="__main__":
    HBNBCommand().cmdloop()

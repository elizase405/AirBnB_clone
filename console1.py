#!/usr/bin/python3

"""
Title: Command interpreter
Description: for debugging and development (front-end use here)
Authors: Elizabeth Akindele & Idoko Attah
"""

# import BaseModel from base_model/models.base_model import BaseModel
import cmd
from shlex import split as sp; import shlex
# import filestorage from engine/models import storage
# from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class definition """

    # base_inheritance = ["BaseModel"]
    classes = ["BaseModel", "User"]
    prompt = "(hbnb) "  # custom prompt given

    # implementing the quit, EOF, and help commands
    def do_quit(self, line):
        """
        cmd method for quitting the program
        """
        return True

    def do_EOF(self, line):
        """
        cmd method for exiting the program
        """
        print()  # print an empty line
        return True

    def help_quit(self):
        """
        cmd help method
        """
        print("Quit command to exit the program")
        print()  # prints an empty line

    # command interpreter updates
    def do_create(self, line):
        """
        - Creates a new instance of BaseModel,
        - Saves it (to the JSON file) and
        - Prints the id
        Instructions:
            - if className arg is missing, print "** class name missing **"
            - If className doesn’t exist, print "** class doesn't exist **"
        """
        line_args = sp(line)

        # checking if className was entered
        if len(line_args) < 1 or len(line_args) == 0:
            print("** class name missing **")
        elif line_args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = line_args[0]
            new_obj = eval(class_name + "()")
            storage.save()  # save the new instance
            print(new_obj.id)

    def do_show(self, line):
        """
        Prints the str representation of an instance based on
        the class name and id
        Instructions:
            - if className arg is missing, print "** class name missing **"
            - If className doesn’t exist, print "** class doesn't exist **"
            - If the id is missing, print "** instance id missing **"
            - If the instance of the class name doesn’t exist for the id,
              print "** no instance found **"
        """
        line_args = sp(line)
        # checking if className was entered
        if len(line_args) < 1 or len(line_args) == 0:
            print("** class name missing **")
        elif line_args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line_args) < 2:  # checking for instance id
            print("** instance id missing **")
        else:
            obj_dict = storage.all()  # retrieve storage content
            classId = line_args[0] + "." + line_args[1]
            if classId in obj_dict:
                instance = obj_dict[classId]
                # printing the value of class.Id
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Prints the str representation of an instance based on
        the class name and id
        Instructions:
            - if className arg is missing, print "** class name missing **"
            - If className doesn’t exist, print "** class doesn't exist **"
            - If the id is missing, print "** instance id missing **"
            - If the instance of the class name doesn’t exist for the id,
              print "** no instance found **"
        """
        line_args = sp(line)
        # checking if className was entered
        if len(line_args) < 1 or len(line_args) == 0:
            print("** class name missing **")
        elif line_args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line_args) < 2:  # checking for instance id
            print("** instance id missing **")
        else:
            obj_dict = storage.all()  # retrieve storage content
            classId = line_args[0] + "." + line_args[1]
            if classId in obj_dict:
                del obj_dict[classId]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name
        Instructions:
            - The printed result must be a list of strings
            - If the class name doesn’t exist,
              print "** class doesn't exist **"
        """
        line_args = sp(line)
        obj_dict = storage.all()  # retrieve storage content

        # if no specific class name, print all
        if len(line_args) < 1 or len(line_args) == 0:
            for classId, val in obj_dict.items():
                print(str(val))
        elif line_args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for classId, val in obj_dict.items():
                if line_args[0] == classId.split('.')[0]:
                    print(str(val))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        Summary:
            update <class name> <id> <attribute name> "<attribute value>"

        """
        line_args = sp(line)
        # checking if className was entered
        if len(line_args) < 1 or len(line_args) == 0:
            print("** class name missing **")
        elif line_args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line_args) < 2:  # checking for instance id
            print("** instance id missing **")
        else:
            obj_dict = storage.all()  # retrieve storage content
            classId = line_args[0] + "." + line_args[1]
            # considering the Summary above
            if classId not in obj_dict:
                print("** no instance found **")
            elif len(line_args) < 3:
                print("** attribute name is missing **")
            elif len(line_args) < 4:
                print("** value missing **")
            else:
                update_obj = obj_dict[classId]
                # setting the attribute name and value
                a_name = line_args[2]
                a_val = line_args[3]
                # using the appropriate value type "eval"
                try:
                    a_val = eval(a_val)
                except (SyntaxError, NameError, SyntaxError, TypeError):
                    a_val = a_val
                # except Exception:
                #    pass

                # updating and saving the object
                setattr(update_obj, a_name, a_val)
                update_obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

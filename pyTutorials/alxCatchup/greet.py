import cmd

class SayHello(cmd.Cmd):
    def do_greet(self, person):
        """
        Greet a person
        """
        if person:
            print("Hi, {}".format(person))
        else:
            print("Hello")

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    SayHello().cmdloop()
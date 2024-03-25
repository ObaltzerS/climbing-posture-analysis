import cmd
import os

class Interface (cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.os = os
        self.prompt = ">>> "
        self.intro = "input filename: input <filename>"

    def do_input(self, args):
        """
        parse filename and run posture recognition
        """
        if (args.endswith(".mp4") and self.os.path.exists(args)):
            print("running with: " + args)
        else:
            print("invalid file type or does not exist")
    def do_exit(self, args):
        return True
    

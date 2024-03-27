import cmd
import os
import classes.analyzer as an

class Interface (cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.os = os
        self.an = an.analyzer()
        self.prompt = ">>> "
        self.intro = "input filename: input <filename>"

    def do_input(self, args):
        """
        parse filename and run posture recognition
        """
        if (args.endswith(".mp4") and self.os.path.exists(args)):
            self.an.getFile(args)
            print("running with: " + args)
        else:
            print("invalid file type or does not exist")

    def do_run(self, args):
        """
        run posture recognition
        """
        self.an.processVideo()

    def do_exit(self, args):
        return True
    

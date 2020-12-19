class SimpleLoadingBar:
    def __init__(self):
        self.prog = 0.  # Floatingpoint
        self.msg = ""
        self.maxout = 0

    def set(self, prog, **kwar):
        """
        Sets progress and message. If message is not defined then the message
        won't be changed.
        """
        if "msg" in kwar:
            self.msg = kwar["msg"]
        self.prog = prog
        out = "\r[{0}{1}]{2:<6} {3}".format(
            "#"*int(20*self.prog),
            " "*(20-int(20*self.prog)),
            str(round(self.prog*100, 2)) + "%",
            self.msg)
        if self.maxout > len(out):
            out += " "*(self.maxout-len(out))
        else:
            self.maxout = len(out)
        print(out, end="")

    def step(self, stepsize=0.01, **kwar):
        """
        Makes one step. Does not update message if message is not defined.
        """
        if "msg" in kwar:
            self.msg = kwar["msg"]
        self.set(self.prog + stepsize)

    def start(self, **kwar):
        """
        Start a new loadingbar.
        """
        self.prog = 0.
        self.maxout = 0
        self.msg = ""
        if "msg" in kwar:
            self.msg = kwar["msg"]
        self.set(self.prog)

    def finish(self, **kwar):
        """
        Sets progress to 100% and updates message. If message is not defined then
        the message won't be changed.
        """
        self.prog = 1
        if "msg" in kwar:
            self.msg = kwar["msg"]
        out = "\r[{0}]{1}% {2}".format("#"*20, self.prog*100, self.msg)
        if self.maxout > len(out):
            out += " "*(self.maxout-len(out))
        else:
            self.maxout = len(out)
        print(out)

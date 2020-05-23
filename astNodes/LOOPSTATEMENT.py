from astNodes.STATEMENT import STATEMENT
from astNodes.WAITSTATEMENT import WAITSTATEMENT
from libs.node import Node


class LOOPSTATEMENT(Node):

    def __init__(self):
        self.ms = None
        self.statements = []
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("do every")
        self.ms = int(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next("ms")
        self.tokenizer.get_and_check_next(":")

        while not self.tokenizer.check_token("end loop"):
            if self.tokenizer.check_token("wait"):
                s = WAITSTATEMENT()
            else:
                s = STATEMENT()
            s.parse()
            self.statements.append(s)

        self.tokenizer.get_and_check_next("end loop")

    def evaluate(self, counter):
        wait = 0
        loop_code = f"\n\
    def loop{counter}(self, dt):\n"
        for s in self.statements:
            if isinstance(s, WAITSTATEMENT):
                wait += s.ms/1000
            else:
                loop_code = loop_code + s.evaluate(wait) + "\n"
        return loop_code, f"self.loop{counter}", self.ms/1000

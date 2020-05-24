from libs.node import Node
from objects.block import DEFAULT_BLOCK_WIDTH, DEFAULT_BLOCK_HEIGHT, Block, GOAL


class MAKESTATEMENT(Node):

    def __init__(self):
        self.block = None
        self.block_name = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("make a")

        block_type = self.tokenizer.get_and_check_next("block|goal")

        self.tokenizer.get_and_check_next("called")
        self.block_name = self.tokenizer.get_next()

        block_width = DEFAULT_BLOCK_WIDTH
        block_height = DEFAULT_BLOCK_HEIGHT
        if self.tokenizer.check_token("with size"):
            self.tokenizer.get_and_check_next("with size")
            block_width = int(self.tokenizer.get_next())
            self.tokenizer.get_and_check_next(",")
            block_height = int(self.tokenizer.get_next())

        self.tokenizer.get_and_check_next("at")
        block_x = int(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next(",")
        block_y = int(self.tokenizer.get_next())

        self.block = Block(block_type, block_x, block_y, block_width, block_height)

    def evaluate(self, wait=None):
        if wait is not None:
            return ''.join((f"        pyglet.clock.schedule_once(lambda dt: setattr(",
                            f"self, '{self.block_name}', MutableBlock(",
                            f"self.window, ({self.block.x}, {self.block.y}))), {wait})"))
        else:
            return ''.join((f"        self.{self.block_name} = MutableBlock(",
                            f"self.window, ({self.block.x}, {self.block.y})",
                            f"{', is_goal=True' if self.block.type == GOAL else ''})"))

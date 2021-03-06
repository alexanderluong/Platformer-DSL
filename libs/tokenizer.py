"""
Code Authorship Acknowledgement:
The tokenizer that we implemented was heavily based off the tokenizer that we have seen in class.
A few points to consider, however, are:
1. The tokenizer was written from scratch, since we had to translate into Python from Java.
2. There were changes to the tokenize method to handle whitespaces in our language.
3. Our project was quite substantial in that most of the time was spent on parsing, building the game, and implementing
   the loop functionality, all of which were original work.
"""
import re


class Tokenizer:

    program = None
    literals = None
    the_tokenizer = None

    def __init__(self, filename: str, literals_list: list):
        Tokenizer.literals = literals_list
        self.tokens = None
        self.current_token = 0
        try:
            with open(filename) as f:
                Tokenizer.program = f.read()
        except OSError:
            print("Didn't find file")
            exit()
        self.__tokenize()

    """
    Parses through the input string and tokenizes it into literals and user-inputs
    """
    def __tokenize(self):
        rw = "~"
        tokenized_program = self.program.replace("\n", "")
        print(tokenized_program)
        for s in self.literals:
            tokenized_program = tokenized_program.replace(s, rw + s + rw)
            print(tokenized_program)
        tokenized_program = tokenized_program.replace(rw + " ", rw)
        print(tokenized_program)
        tokenized_program = tokenized_program.replace(rw + rw, rw)
        print(tokenized_program)
        if len(tokenized_program) > 0 and tokenized_program[0] == rw:
            tokenized_program = tokenized_program[1:]
        if len(tokenized_program) > 0 and tokenized_program[-1] == rw:
            tokenized_program = tokenized_program[:-1]
        self.tokens = tokenized_program.split(rw)
        print(self.tokens)
        for i in range(len(self.tokens)):
            self.tokens[i] = self.tokens[i].strip()
        print(self.tokens)
        self.tokens = list(filter(None, self.tokens))
        print(self.tokens)

    """
    Returns the current token
    """
    def __check_next(self):
        token = ""
        if self.current_token < len(self.tokens):
            token = self.tokens[self.current_token]
        else:
            token = "NO_MORE_TOKENS"
        return token

    """
    Returns the current token
    Advances self.current_token by 1
    """
    def get_next(self):
        token = ""
        if self.current_token < len(self.tokens):
            token = self.tokens[self.current_token]
            self.current_token += 1
        else:
            token = "NULLTOKEN"
        return token

    """
    Returns true if the current token matches the given regexp
    """
    def check_token(self, regexp: str):
        s = self.__check_next()
        print("comparing: |" + s + "|  to  |" + regexp + "|")
        return re.match(regexp, s) is not None

    """
    Checks if the current token matches the given regexp, returns it if true
    Otherwise, throws an error
    """
    def get_and_check_next(self, regexp: str):
        s = self.get_next()
        if re.match(regexp, s) is None:
            raise Exception("Unexpected next token for Parsing! Expected something matching: " + regexp + " but got: " + s)
        print("matched: " + s + "  to  " + regexp)
        return s

    """
    Returns true if there are more tokens
    """
    def more_tokens(self):
        return self.current_token < len(self.tokens)

    """
    Creates the singleton instance
    """
    @staticmethod
    def make_tokenizer(filename: str, literals: list):
        if Tokenizer.the_tokenizer is None:
            Tokenizer.the_tokenizer = Tokenizer(filename, literals)

    """
    Returns the singleton instance if existing, instantiates and returns it if not
    """
    @staticmethod
    def get_tokenizer():
        return Tokenizer.the_tokenizer

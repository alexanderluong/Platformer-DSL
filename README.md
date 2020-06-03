## What is Platformer DSL?
Platformer DSL is a project that I and three others completed for our CPSC 410 (Advanced Software Engineering) course. Our project was to create a DSL that would build a game level. It would  allows users with a basic knowledge of programming to build a simple Mario-like platformer game. Players win the game when they reach a flag.

Features of the DSL include:
* timed loops 
* dynamic game arena size
* moving blocks
* destroying blocks

The project was built using Python3 and the [Arcade library](https://arcade.academy/).

## Installation Instructions
1. Install [Python3](https://www.python.org/downloads/)
2. Install the Arcade library by running ```pip3 install arcade``` in terminal
3. Run ```git clone``` on the project repository
4. In terminal, run ```cd Platformer-DSL```

## Usage
1. Edit the config.txt file (following the EBNF) with desired input
2. Run ```python3 main.py``` to see the input DSL get translated into a game

## EBNF
            PROGRAM ::= CONFIGUREARENA? SETPLAYERPOS? (STATEMENT | LOOPSTATEMENT)+
     CONFIGUREARENA ::= "arena size" DIGITTUPLE
       SETPLAYERPOS ::= "put player at" DIGITTUPLE
         DIGITTUPLE ::= DIGIT "," DIGIT // e.g. xpos, ypos
          STATEMENT ::= MAKESTATEMENT | MODIFYSTATMENT
      MAKESTATEMENT ::= "make a" BLOCKTYPE "called" BLOCKNAME "at" DIGITTUPLE
    MODIFYSTATEMENT ::= REMOVESTATEMENT | SETSTATEMENT | CHANGESTATEMENT | MOVESTATEMENT
    REMOVESTATEMENT ::= "destroy" BLOCKNAME
       SETSTATEMENT ::= "set" FIELD "of" BLOCKNAME "to" DIGIT
    CHANGESTATEMENT ::= "change" FIELD "of" BLOCKNAME "by" DIGIT
      MOVESTATEMENT ::= "move" BLOCKNAME DIR "by" DIGIT
      LOOPSTATEMENT ::= "do every" DIGIT TIME ":" (STATEMENT | WAITSTATEMENT)+ "end loop"
      WAITSTATEMENT ::= "wait" DIGIT TIME
               TIME ::= "ms"
          BLOCKTYPE ::= "block" | "goal"
          BLOCKNAME ::= STRING
                DIR ::= "up" | "down" | "left" | "right"
              FIELD ::= POSITION
           POSITION ::= "xpos" | "ypos"
              DIGIT ::= (-)?[0-9]+
            STRING ::= [A-Za-z0-9]+

## Preview
![Game Preview](/images/preview.png)

## Code Authorship Acknowledgement
The tokenizer that we implemented was heavily based off the tokenizer that we have seen in class.
A few points to consider, however, are:
1. The tokenizer was written from scratch, since we had to translate into Python from Java.
2. There were changes to the tokenize method to handle whitespaces in our language.
3. Our project was quite substantial in that most of the time was spent on parsing, building the game, and implementing the loop functionality, all of which were original work.

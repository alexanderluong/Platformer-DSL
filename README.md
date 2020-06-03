### Overview
Our project is building a game level design DSL that allows users with a basic knowledge of programming to build a simple Mario-like platformer game.

### EBNF
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

### Preview
![Game Preview](/images/preview.png)

### Code Authorship Acknowledgement
The tokenizer that we implemented was heavily based off the tokenizer that we have seen in class.
A few points to consider, however, are:
1. The tokenizer was written from scratch, since we had to translate into Python from Java.
2. There were changes to the tokenize method to handle whitespaces in our language.
3. Our project was quite substantial in that most of the time was spent on parsing, building the game, and implementing the loop functionality, all of which were original work.

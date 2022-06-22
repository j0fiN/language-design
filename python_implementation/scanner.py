
from enum import Enum, auto

class TokenType(Enum):
    # EXPRESSION
    TOKEN_LEFT_PAREN = auto()
    TOKEN_RIGHT_PAREN = auto()
    TOKEN_LEFT_BRACE = auto()
    TOKEN_RIGHT_BRACE = auto()
    TOKEN_COMMA = auto()
    TOKEN_DOT = auto()
    TOKEN_MINUS = auto()
    TOKEN_PLUS = auto()
    TOKEN_SEMICOLON = auto()
    TOKEN_SLASH = auto()
    TOKEN_STAR = auto()
    TOKEN_POW = auto()

 # One or two character tokens.
    TOKEN_BANG = auto()
    TOKEN_BANG_EQUAL = auto()
    TOKEN_EQUAL = auto()
    TOKEN_EQUAL_EQUAL = auto()
    TOKEN_GREATER = auto()
    TOKEN_GREATER_EQUAL = auto()
    TOKEN_LESS = auto()
    TOKEN_LESS_EQUAL = auto()

 # Literals.
    TOKEN_IDENTIFIER = auto()
    TOKEN_STRING = auto()
    TOKEN_NUMBER = auto()

 # Keywords.
    TOKEN_AND = auto()
    TOKEN_CLASS = auto()
    TOKEN_ELSE = auto()
    TOKEN_FALSE = auto()
    TOKEN_FOR = auto()
    TOKEN_FUN = auto()
    TOKEN_IF = auto()
    TOKEN_NIL = auto()
    TOKEN_OR = auto()
    TOKEN_PRINT = auto()
    TOKEN_RETURN = auto()
    TOKEN_SUPER = auto()
    TOKEN_THIS = auto()
    TOKEN_TRUE = auto()
    TOKEN_VAR = auto()
    TOKEN_WHILE = auto()

    TOKEN_ERROR = auto()
    TOKEN_EOF = auto()


    def __repr__(self) -> str:
        return self.name


class Token:
    
    def __init__(self, _type, start, length, line) -> None:
        self.type = _type
        self.start = start
        self.length = length
        self.line = line

    def __repr__(self) -> str:
        return str(self.__dict__)


class Scanner:

    def __init__(self, source) -> None:
        self.start = 0
        self.current = 0
        self.line = 1
        self.source = source
        self.length = len(self.source)
    

    def isAtEnd(self):
        return self.current == self.length
    
    def peekAtEnd(self):
        return self.current + 1 == self.length

    def makeToken(self, _type):
        return Token(
            _type, 
            self.source[self.start: self.current + 1] \
                if _type != TokenType.TOKEN_EOF else "",
            self.current - self.start + 1, 
            self.line
            )

    def errorToken(self, message):
        return Token(
            TokenType.TOKEN_ERROR, 
            message,
            len(message),
            self.line
        )

    def match(self, expected):
        if self.isAtEnd(): return False
        if self.peekAtEnd(): return False
        if self.source[self.current + 1] != expected: return False
        self.current += 1
        return True
        


    def scanToken(self):
        self.start = self.current

        if self.isAtEnd(): return self.makeToken(TokenType.TOKEN_EOF)

        char = self.source[self.current]

        if char in [' ', '\r', '\t']:
            while not self.isAtEnd() and  self.source[self.current] in [' ', '\r', '\t']:
                self.current += 1
                if self.isAtEnd(): return self.makeToken(TokenType.TOKEN_EOF)
            return 

        if char in '\n':
            while not self.isAtEnd() and self.source[self.current] == '\n':
                self.current += 1
                self.line += 1
                if self.isAtEnd(): return self.makeToken(TokenType.TOKEN_EOF)
            return
        

        if char == '(': return self.makeToken(TokenType.TOKEN_LEFT_PAREN)
        elif char == ')': return self.makeToken(TokenType.TOKEN_RIGHT_PAREN)
        elif char == '{': return self.makeToken(TokenType.TOKEN_LEFT_BRACE)
        elif char == '}': return self.makeToken(TokenType.TOKEN_RIGHT_BRACE)
        elif char == ';': return self.makeToken(TokenType.TOKEN_SEMICOLON)
        elif char == '.': return self.makeToken(TokenType.TOKEN_DOT)
        elif char == ',': return self.makeToken(TokenType.TOKEN_COMMA)
        elif char == '-': return self.makeToken(TokenType.TOKEN_MINUS)
        elif char == '+': return self.makeToken(TokenType.TOKEN_PLUS)
        elif char == '/': 
            if self.match('/'):
                while not self.isAtEnd() and self.source[self.current] != '\n':
                    self.current += 1
                    if self.isAtEnd(): return self.makeToken(TokenType.TOKEN_EOF)
                return 
            elif self.match('*'):
                while not self.isAtEnd() and not (self.source[self.current] == '/' and self.source[self.current - 1] == '*'):
                    self.current += 1
                    if self.isAtEnd: return self.makeToken(TokenType.TOKEN_EOF)
                self.current += 1
                return


                
                


            return self.makeToken(TokenType.TOKEN_SLASH)
        elif char == '*': return self.makeToken(TokenType.TOKEN_STAR)
        elif char == '^': return self.makeToken(TokenType.TOKEN_POW)

        elif char == '!':
            if self.match('='):
                return self.makeToken(TokenType.TOKEN_BANG_EQUAL)
            else:
                return self.makeToken(TokenType.TOKEN_BANG)
        
        elif char == '=':
            if self.match('='):
                return self.makeToken(TokenType.TOKEN_EQUAL_EQUAL)
            else:
                return self.makeToken(TokenType.TOKEN_EQUAL)
            
        elif char == '<':
            if self.match('='):
                return self.makeToken(TokenType.TOKEN_LESS_EQUAL)
            else:
                return self.makeToken(TokenType.TOKEN_LESSER)
        
        elif char == '>':
            if self.match('='):
                return self.makeToken(TokenType.TOKEN_GREATER_EQUAL)
            else:
                return self.makeToken(TokenType.TOKEN_GREATER)



        return self.errorToken("Expected character.")


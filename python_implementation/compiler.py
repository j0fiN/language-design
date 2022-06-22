from scanner import Scanner
from scanner import *
class Compiler:

    def __init__(self) -> None:
        ...
    
    def compile(self, source):
        scanner = Scanner(source)
        line = -1
        while True:
            token = scanner.scanToken()
            scanner.current += 1
            if token and token.line != line:
                print(f"{token.line} ", end = '\t')
                line = token.line
            else:
                print(" | ", end = '\t') if token else ...
            
            print(f"{token.type.name} '{token.length}' {token.start}") if token else ...

            if token and token.type == TokenType.TOKEN_EOF: break



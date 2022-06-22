import sys

INFO = '\033[96m'
ENDC = '\033[0m'
FAIL = '\033[91m'

fail = lambda msg: print(f"{FAIL} {msg} {ENDC}")

info = lambda msg: print(f"{INFO} {msg} {ENDC}")


class Interpreter:

    def __init__(self) -> None:
        self.stack = []

    def interpret(self, line: str) -> float:
        postfix = self.parser(line)
        print(self.stack)
        # self.evaluate(postfix)
    
    def parser(self, line):
        '''
        (1 * (2 - 3) + 1) * 3 / 4
        (1 * (2 * 3 * 2)) + 4
        (1 23-)
        *
        '''
        number = []
        operator = []
        stack = []
        line = '(' + line + ')'
        for i in line:
            print("STACK : ", stack)
            print("OPER : ", operator)
            print()
            if i in [' ', '\t', '\r']: continue

            if i.isdigit():
                number.append(i)

            elif i in ['+', '-', '*', '/']:
                stack.append(''.join(number)) if number != [] else ...
                number.clear()
                if operator == []:
                    operator.append(i)

                elif i in ['+', '-']:
                    if operator[-1] in ['*', '/']:
                        while operator[-1] != '(':
                            stack.append(operator.pop())
                        operator.append(i)
                    else:
                        operator.append(i)

                elif i in ['*', '/']:
                    if operator[-1] in ['*', '/']:
                        while operator[-1] not in ['+', '-', '(']:
                            stack.append(operator.pop())
                        operator.append(i)
                    else:
                        operator.append(i)
            elif i == '(':
                stack.append(i)
                operator.append(i)
            
            elif i == ')':
                print('closing')
                stack.append(''.join(number)) if number != [] else ...
                number.clear()
                
                while operator[-1] != '(':
                    stack.append(operator.pop())
                operator.pop()

                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()

                while temp != []:
                    stack.append(temp.pop())




     
        stack.append(''.join(number)) if number != [] else ...
        while operator != []:
            stack.append(operator.pop())

        self.stack = stack.copy()
    
if __name__ == "__main__":    
    I = Interpreter()
    while True:
        try:
            line = input('> ')
            I.interpret(line)
        except KeyboardInterrupt:
            print(info('Thank you for using.'))
            sys.exit(0)


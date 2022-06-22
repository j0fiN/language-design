class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        postfix = self.toPostfix(s)
        for i in postfix:
            if i not in ['+', '*', '-', '/']:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+': res = a + b
                elif i == '-': res = a - b
                elif i == '*': res = a * b
                elif i == '/': res = a // b
                stack.append(res)
        if len(stack) == 1:
            return stack.pop()
        else:
            return ''.join(list(map(str, stack)))
    
    def toPostfix(self, s):
        '''
        BODMAS
        1+2*3+4-5 => 123*+4+5-
        1, 2 
        +, *
        '''

        stack = []
        operator = []
        number = []
        for i in s:
            if i in [' ', '"']: continue
            if i not in ['+', '*', '-', '/']:
                number.append(i)
            else:
                stack.append(''.join(number))
                number = []
                if i == '-' or i == '+':
                    while operator != []:
                        stack.append(operator.pop())
                elif i == '*':
                    while operator != []:
                        if operator[-1] in ['-', '+']: break
                        stack.append(operator.pop())
                else:
                    while operator != []:
                        if operator[-1] in ['-', '+']: break
                        stack.append(operator.pop())
                operator.append(i)
        if number:
            stack.append(''.join(number))
        while operator != []:
            stack.append(operator.pop())
        return stack
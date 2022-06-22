from _chunk import Chunk, OpCode
from enum import Enum
from compiler import Compiler


DEBUG_TRACE_EXECUTION = False

class InterpreterResult:
    INTERPRET_OK = 0
    INTERPRET_COMPILE_ERROR = -1
    INTERPRET_RUNTIME_ERROR = -2



    



class VM:
    def __init__(self) -> None:
        self.chunk = None
        self.ip = None
        self.stack = []

    def freeVM(self):
        ...

    def read_constant(self):
        if not hasattr(self, 'constant_index'):
            self.constant_index = 0
        self.index += 1
        self.constant_index += 1
        return self.chunk.constants.values[self.constant_index - 1]
        

    def binary_op(self, operation):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(eval(str(a) + operation + str(b)))

    def run(self):
        self.index = 0
        while self.index < len(self.ip):
            if DEBUG_TRACE_EXECUTION:
                print("     ")
                for i in self.stack:
                    print('[')
                    print(i)
                    print(']')
                print('\n')
                self.chunk.dissassembleInstruction(self.offset)

            instruction = self.ip[self.index]
            if instruction == OpCode.OP_CONSTANT:
                constant = self.read_constant()
                self.stack.append(constant)
            
            elif instruction == OpCode.OP_ADD: self.binary_op('+')
            elif instruction == OpCode.OP_SUBTRACT: self.binary_op('*')
            elif instruction == OpCode.OP_MULTIPLY: self.binary_op('-')
            elif instruction == OpCode.OP_DIVIDE: self.binary_op('/')

            elif instruction == OpCode.OP_NEGATE:
                self.stack.append(-self.stack.pop())

            elif instruction == OpCode.OP_RETURN:
                print(self.stack.pop())
                return InterpreterResult.INTERPRET_OK
            self.index += 1
        
            
    def interpret(self, source):
        compiler = Compiler()
        compiler.compile(source)
        return InterpreterResult.INTERPRET_OK


    

     
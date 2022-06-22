from dis import disassemble
from enum import Enum, auto
from value import ValueArray
import logging

Vm_link = "https://youtu.be/OjaAToVkoTw"

class OpCode(Enum):
    OP_CONSTANT = auto()
    OP_ADD      = auto()
    OP_SUBTRACT = auto()
    OP_MULTIPLY = auto()
    OP_DIVIDE   = auto()
    OP_NEGATE   = auto()
    OP_RETURN   = auto()
     

class Chunk:
    def __init__(self) -> None:
        self.code = []
        self.constants = ValueArray()
        self.count = 0
        self.lines = []

    @staticmethod
    def getType(obj):
        return type(obj).__name__

    def sameLine(self, offset):
        if offset != 0 and self.lines[offset - 1] == self.lines[offset]:
            return True
        else:
            return False

    def writeChunk(self, _byte, line):
        self.code.append(_byte)
        self.lines.append(line)
        self.count += 1
    
    def addConstant(self, value):
        self.constants.writeValueArray(value)
        return self.constants.count - 1
    
    def freeChunk(self):
        self.code = []
        self.count = 0
        self.lines = []

    # DISASSEMBLER
    def disassembleChunk(self, name: str):
        print(f"== {name} ==")

        offset = 0
        while offset < self.count:
            offset = self.disassembleInstruction(offset)
            

    def disassembleInstruction(self, offset):
        obj = self.code[offset]

        isOpCode: bool = lambda opCode: obj.name == opCode

        if isOpCode("OP_CONSTANT"):
            if not self.sameLine(offset):
                print(f"{obj.value}\t{self.lines[offset]}\t{obj.name}\t{self.code[offset + 1]} '{self.constants.values[self.code[offset + 1]]}'")
            else:
                print(f"{obj.value}\t|\t{obj.name}\t{self.code[offset + 1]} '{self.constants.values[self.code[offset + 1]]}'")
            offset += 2
        
        elif isOpCode("OP_NEGATE"):
            if not self.sameLine(offset):
                print(f"{obj.value}\t{self.lines[offset]}\t{obj.name}")
            else:
                print(f"{obj.value}\t|\t{obj.name}")
            offset += 1
        
        elif isOpCode("OP_ADD") or isOpCode("OP_SUBTRACT") \
            or isOpCode("OP_MULTIPLY") or isOpCode("OP_DIVIDE"):
            if not self.sameLine(offset):
                print(f"{obj.value}\t{self.lines[offset]}\t{obj.name}")
            else:
                print(f"{obj.value}\t|\t{obj.name}")
            offset += 1

        elif isOpCode("OP_RETURN"):
            if not self.sameLine(offset):
                print(f"{obj.value}\t{self.lines[offset]}\t{obj.name}")
            else:
                print(f"{obj.value}\t|\t{obj.name}")
            offset += 1

        else:
            print("No instruction.")
        return offset

    

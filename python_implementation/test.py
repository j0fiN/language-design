from enum import IntEnum, auto

class OpCode(IntEnum):
    OP_CONSTANT     :int
    OP_ADD          :int
    OP_SUBTRACT     :int
    OP_MULTIPLY     :int
    OP_DIVIDE       :int
    OP_NEGATE       :int
    OP_RETURN       :int


print(OpCode.OP_CONSTANT)
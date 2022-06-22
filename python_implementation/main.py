import sys
from _chunk import Chunk, OpCode
from vm import VM, InterpreterResult
import errno

FAIL = '\033[91m'
ENDC = '\033[0m'

'''
vm = VM()
    chunk = Chunk()

    constant = chunk.addConstant(1.2) # adds to values array
    chunk.writeChunk(OpCode.OP_CONSTANT, 123)
    chunk.writeChunk(constant, 123) # adds to chunk array

    constant = chunk.addConstant(3.4)
    chunk.writeChunk(OpCode.OP_CONSTANT, 123)
    chunk.writeChunk(constant, 123)

    chunk.writeChunk(OpCode.OP_ADD, 123)

    constant = chunk.addConstant(5.6)
    chunk.writeChunk(OpCode.OP_CONSTANT, 124)
    chunk.writeChunk(constant, 123)

    chunk.writeChunk(OpCode.OP_DIVIDE, 124)

    chunk.writeChunk(OpCode.OP_NEGATE, 124)

    chunk.writeChunk(OpCode.OP_RETURN, 124)
    chunk.disassembleChunk("test chunk")
    vm.interpret(chunk)
    vm.freeVM()
    chunk.freeChunk()
    return 0
'''

ARGV = sys.argv

def repl():
    while True:
        line = ''
        try:
            line = input(":> ")
        except KeyboardInterrupt:
            sys.exit("Thank you for using pypense")
        finally:
            vm.interpret(line)

def runFile(path):
    source = ''
    try:
        with open(path, 'r') as f:
            source = f.read()
    except:
        sys.stderr.write(FAIL + f"Could not open file {path}" + ENDC)
        sys.exit(64)


    result = vm.interpret(source)

    if result == InterpreterResult.INTERPRET_COMPILE_ERROR: sys.exit(65)
    if result == InterpreterResult.INTERPRET_RUNTIME_ERROR: sys.exit(70)
    
    

def main(argv):
    global vm
    vm = VM()
    argc = len(argv)
    if argc == 1:
        repl()
    elif argc == 2:
        runFile(argv[1])
    else:
        sys.stderr.write(FAIL + "Usage: pypense [path]" + ENDC)
        sys.exit(64)

    vm.freeVM
    


if __name__ == "__main__":
    main(ARGV)
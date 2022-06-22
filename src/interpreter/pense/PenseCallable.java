package interpreter.pense;

import java.util.*;

interface PenseCallable {
    int arity();
    Object call(Interpreter interpreter, List<Object> arguments);
}

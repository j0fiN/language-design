## Grammar
This is called the context-free grammar which will help during parser implementation.
### Mathematical Expressions
```
expression -> literal
            | unary
            | binary
            | grouping ;

literal     -> NUMBER | STRING | "true" | "false" | "nil" ;
grouping    -> "(" expression ")" ;
unary       -> ( "-" | "!" ) expression ;
binary      -> expression operator expression ;
operator    -> "==" | "!=" | "<" | "<=" | ">" | ">=" | "+" | "-" | "*" | "/" ;
```
#### Order of Precedence
```
Name        Operators       Associates
Equality    == !=           Left
Comparison  > >= < <=       Left
Term        - +             Left
Factor      / *             Left
Unary       ! -             Right
```

### Complete Expressions Grammar (with example)
```
expression  -> equality ;
equality    -> comparison ( ( "!=" | "==" ) comparison )* ;
comaprison  -> term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term        -> factor ( ( "-" | "+" ) factor )* ;
factor      -> unary ( ( "/" | "*" ) unary )* ;
unary       -> ( "!" | "-" ) unary
            | primary
primary     -> NUMBER | STRING | "true" | "false" | "none"
            | "(" expression ")" ;
```

#### Pense dynamic typed vs. Java
```
Lox type        Java representation
Any Lox value   Object
none            null
Boolean         Boolean
number          Double
string          String
```

### statement rules
```
program     -> declaration* EOF ;
declaration -> varDecl
            | statement;
varDecl     -> "var" IDENTIFIER ( "=" expression )? ";" ;
statement   -> exprStmt
            | ifStmt
            | printStmt 
            | returnStmt
            | whileStmt 
            | block ;
whileStmt → "while" "(" expression ")" statement ;
ifStmt      -> "if" "(" expression ")" statement
            ( "else" statement )? ;
block       -> "{" declaration* "}" ;
exprStmt    -> expression ";" ;
printStmt   -> "print" expression ";" ;
primary     -> "true" | "false" | "none"
            | NUMBER | STRING
            | "(" expression ")"
            | IDENTIFIER ;
```

### Assignment Syntax
```
expression      → assignment ;
assignment      → IDENTIFIER "=" assignment
                | logic_or ;
logic_or        → logic_and ( "or" logic_and )* ;
logic_and       → equality ( "and" equality )* ;
```

### Function Calls
```
unary       → ( "!" | "-" ) unary | call ;
call        → primary ( "(" arguments? ")" )* ;
arguments → expression ( "," expression )* ;
```

### Function Declaration
```
declaration     → funDecl
                | varDecl
                | statement ;
funDecl         → "fn" function ;
function        → IDENTIFIER "(" parameter? ")" block ;
returnStmt → "return" expression? ";" ;
```
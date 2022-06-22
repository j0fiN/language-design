///*
//* Just to show the representation of the AST syntax tree...that's all
//* Not a part of the interpreter design.
//* */
//package interpreter.pense;
//
//
//
//class AstPrinter implements Expr.Visitor<String> {
//    String print(Expr expr) {
//        return expr.accept(this);
//    }
//    @Override
//    public String visitLogicalExpr(Expr.Logical expr) {
//        return "";
//    }
//
//    @Override
//    public Void visitExprCall(Expr.Call expr) {
//        return;
//    }
//
//    @Override
//    public String visitAssignExpr(Expr.Assign expr) {return "";}
//
//    @Override
//    public String visitVariableExpr(Expr.Variable expr) {
//        return "";
//    }
//
//    @Override
//    public String visitBinaryExpr(Expr.Binary expr) {
//        return parenthesize(expr.operator.lexeme, expr.left, expr.right);
//    }
//
//    @Override
//    public String visitGroupingExpr(Expr.Grouping expr) {
//        return parenthesize("group", expr.expression);
//    }
//    @Override
//    public String visitLiteralExpr(Expr.Literal expr) {
//        if (expr.value == null) return "none";
//        return expr.value.toString();
//    }
//    @Override
//    public String visitUnaryExpr(Expr.Unary expr) {
//        return parenthesize(expr.operator.lexeme, expr.right);
//    }
//
//    private String parenthesize(String name, Expr... exprs) {
//        StringBuilder builder  = new StringBuilder();
//
//        builder.append("(").append(name);
//        for (Expr expr: exprs) {
//            builder.append(" ");
//            builder.append(expr.accept(this));
//        }
//        builder.append(")");
//
//        return builder.toString();
//    }
//
//
//    // TEST
//    public static void main(String[] args) {
//        Expr expression = new Expr.Binary(
//                new Expr.Unary(
//                        new Token(TokenType.MINUS, "-", null, 1),
//                        new Expr.Literal(123)),
//                new Token(TokenType.STAR, "*", null, 1),
//                new Expr.Grouping(
//                        new Expr.Literal(45.67)));
//        System.out.println(new AstPrinter().print(expression));
//    }
//}
# Generated from VarExpr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VarExprParser import VarExprParser
else:
    from VarExprParser import VarExprParser

# This class defines a complete listener for a parse tree produced by VarExprParser.
class VarExprListener(ParseTreeListener):

    # Enter a parse tree produced by VarExprParser#expr.
    def enterExpr(self, ctx:VarExprParser.ExprContext):
        pass

    # Exit a parse tree produced by VarExprParser#expr.
    def exitExpr(self, ctx:VarExprParser.ExprContext):
        pass



del VarExprParser
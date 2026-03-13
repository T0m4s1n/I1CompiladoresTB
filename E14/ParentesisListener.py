# Generated from Parentesis.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ParentesisParser import ParentesisParser
else:
    from ParentesisParser import ParentesisParser

# This class defines a complete listener for a parse tree produced by ParentesisParser.
class ParentesisListener(ParseTreeListener):

    # Enter a parse tree produced by ParentesisParser#expr.
    def enterExpr(self, ctx:ParentesisParser.ExprContext):
        pass

    # Exit a parse tree produced by ParentesisParser#expr.
    def exitExpr(self, ctx:ParentesisParser.ExprContext):
        pass


    # Enter a parse tree produced by ParentesisParser#term.
    def enterTerm(self, ctx:ParentesisParser.TermContext):
        pass

    # Exit a parse tree produced by ParentesisParser#term.
    def exitTerm(self, ctx:ParentesisParser.TermContext):
        pass


    # Enter a parse tree produced by ParentesisParser#factor.
    def enterFactor(self, ctx:ParentesisParser.FactorContext):
        pass

    # Exit a parse tree produced by ParentesisParser#factor.
    def exitFactor(self, ctx:ParentesisParser.FactorContext):
        pass



del ParentesisParser
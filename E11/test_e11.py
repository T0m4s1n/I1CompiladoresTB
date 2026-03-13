from antlr4 import *
from Expr1Lexer import Expr1Lexer
from Expr1Parser import Expr1Parser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = Expr1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Expr1Parser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('1+2+3')
    test('5+6+7+8')

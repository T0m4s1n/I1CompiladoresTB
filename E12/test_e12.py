from antlr4 import *
from Expr2Lexer import Expr2Lexer
from Expr2Parser import Expr2Parser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = Expr2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Expr2Parser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('3+4*5')
    test('2*3+4')

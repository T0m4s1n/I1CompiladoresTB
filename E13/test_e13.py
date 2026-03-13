from antlr4 import *
from Expr3Lexer import Expr3Lexer
from Expr3Parser import Expr3Parser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = Expr3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Expr3Parser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('3+4*5')

from antlr4 import *
from VarExprLexer import VarExprLexer
from VarExprParser import VarExprParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = VarExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = VarExprParser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('x+5')
    test('y+10')

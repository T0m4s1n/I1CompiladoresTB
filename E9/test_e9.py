from antlr4 import *
from SumaLexer import SumaLexer
from SumaParser import SumaParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = SumaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SumaParser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('3+4')
    test('5+10')

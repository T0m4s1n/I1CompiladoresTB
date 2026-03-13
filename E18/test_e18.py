from antlr4 import *
from PrintLexer import PrintLexer
from PrintParser import PrintParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = PrintLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PrintParser(token_stream)
    tree = parser.stat()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('print x')
    test('print 5')

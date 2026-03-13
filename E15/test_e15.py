from antlr4 import *
from AsignacionLexer import AsignacionLexer
from AsignacionParser import AsignacionParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = AsignacionLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AsignacionParser(token_stream)
    tree = parser.stat()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('x = 5')
    test('y = 10')

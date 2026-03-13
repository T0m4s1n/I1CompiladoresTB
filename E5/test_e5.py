from antlr4 import *
from SaludoLexer import SaludoLexer
from SaludoParser import SaludoParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = SaludoLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SaludoParser(token_stream)
    tree = parser.saludo()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('hola Juan')
    test('hola Maria')

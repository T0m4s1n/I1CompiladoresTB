from antlr4 import *
from NumerosLexer import NumerosLexer
from NumerosParser import NumerosParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = NumerosLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = NumerosParser(token_stream)
    tree = parser.numero()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test("5")
    test("20")
    test("100")
    test("3456")

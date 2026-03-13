from antlr4 import *
from IdentificadorLexer import IdentificadorLexer
from IdentificadorParser import IdentificadorParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = IdentificadorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = IdentificadorParser(token_stream)
    tree = parser.id_()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test("x")
    test("variable")
    test("contador")
    test("valor1")

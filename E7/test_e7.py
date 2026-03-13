from antlr4 import *
from ListaNumerosLexer import ListaNumerosLexer
from ListaNumerosParser import ListaNumerosParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = ListaNumerosLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ListaNumerosParser(token_stream)
    tree = parser.lista()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('1 2 3')
    test('5 10 15')

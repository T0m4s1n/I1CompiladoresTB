from antlr4 import *
from ListaComasLexer import ListaComasLexer
from ListaComasParser import ListaComasParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = ListaComasLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ListaComasParser(token_stream)
    tree = parser.lista()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('1,2,3')
    test('5,10,15')

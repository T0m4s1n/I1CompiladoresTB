from antlr4 import *
from Saludo2Lexer import Saludo2Lexer
from Saludo2Parser import Saludo2Parser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = Saludo2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Saludo2Parser(token_stream)
    tree = parser.saludo()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('hola Juan')
    test('buenosdias Pedro')

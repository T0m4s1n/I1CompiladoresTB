from antlr4 import *
from OperadoresLexer import OperadoresLexer
from OperadoresParser import OperadoresParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = OperadoresLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OperadoresParser(token_stream)
    tree = parser.op()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test("+")
    test("-")
    test("*")
    test("/")

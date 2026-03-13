from antlr4 import *
from MiniLexer import MiniLexer
from MiniParser import MiniParser

def test(input_str):
    print(f"\nPrueba con:\n{input_str}")
    input_stream = InputStream(input_str)
    lexer = MiniLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniParser(token_stream)
    tree = parser.prog()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('x = 5\ny = 10\nprint x\nprint y')

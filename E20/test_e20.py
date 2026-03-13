from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser

def test(input_str):
    print(f"\nPrueba con:\n{input_str}")
    input_stream = InputStream(input_str)
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)
    tree = parser.prog()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('x = 5\ny = 10\nprint x + y\nprint (x + y) * 2')

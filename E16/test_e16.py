from antlr4 import *
from ProgramaLexer import ProgramaLexer
from ProgramaParser import ProgramaParser

def test(input_str):
    print(f"\nPrueba con:\n{input_str}")
    input_stream = InputStream(input_str)
    lexer = ProgramaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ProgramaParser(token_stream)
    tree = parser.prog()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('x=5\ny=10\nz=20')

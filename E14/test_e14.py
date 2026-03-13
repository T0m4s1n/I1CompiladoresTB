from antlr4 import *
from ParentesisLexer import ParentesisLexer
from ParentesisParser import ParentesisParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = ParentesisLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ParentesisParser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('(3+4)*5')

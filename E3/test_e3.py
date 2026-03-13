from antlr4 import *
from KeywordsLexer import KeywordsLexer
from KeywordsParser import KeywordsParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = KeywordsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = KeywordsParser(token_stream)
    tree = parser.stat()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test("if")
    test("while")
    test("print")

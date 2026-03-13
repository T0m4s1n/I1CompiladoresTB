from antlr4 import *
from SumaRestaLexer import SumaRestaLexer
from SumaRestaParser import SumaRestaParser

def test(input_str):
    print(f"\nPrueba con: '{input_str}'")
    input_stream = InputStream(input_str)
    lexer = SumaRestaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SumaRestaParser(token_stream)
    tree = parser.expr()
    print(f"Resultado: {tree.toStringTree(recog=parser)}")

if __name__ == '__main__':
    test('5+3')
    test('8-2')

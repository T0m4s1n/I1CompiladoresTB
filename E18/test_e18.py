from antlr4 import *
from PrintLexer import PrintLexer
from PrintParser import PrintParser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = PrintLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = PrintParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = PrintParser(token_stream)
    tree = parser.stat()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["print x", "print 5"]
    for i in inputs:
        test(i)

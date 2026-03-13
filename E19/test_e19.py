from antlr4 import *
from MiniLexer import MiniLexer
from MiniParser import MiniParser

def test(input_str):
    print(f"PRUEBA:\n{input_str}")
    
    input_stream = InputStream(input_str)
    
    lexer = MiniLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = MiniParser.symbolicNames[token.type]
            print(f"Texto: {repr(token.text):<10} Tipo: {token_name}")
    
    parser = MiniParser(token_stream)
    tree = parser.prog()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["x = 5\ny = 10\nprint x\nprint y"]
    for i in inputs:
        test(i)

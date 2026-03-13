from antlr4 import *
from KeywordsLexer import KeywordsLexer
from KeywordsParser import KeywordsParser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = KeywordsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = KeywordsParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    

    parser = KeywordsParser(token_stream)
    tree = parser.stat()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["if", "while", "print"]
    for i in inputs:
        test(i)

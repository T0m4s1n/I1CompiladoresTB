from antlr4 import *
from KeywordsLexer import KeywordsLexer
from KeywordsParser import KeywordsParser

def test(input_str):
    print(f"\n" + "="*30)
    print(f"PRUEBA: '{input_str}'")
    print("="*30)
    
    input_stream = InputStream(input_str)
    
    # Lexer
    lexer = KeywordsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    print("\nTOKENS GENERADOS:")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = KeywordsParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    # Parser
    parser = KeywordsParser(token_stream)
    tree = parser.stat()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["if", "while", "print"]
    for i in inputs:
        test(i)

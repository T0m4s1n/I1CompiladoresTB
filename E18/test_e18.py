from antlr4 import *
from PrintLexer import PrintLexer
from PrintParser import PrintParser

def test(input_str):
    print(f"\n" + "="*30)
    print(f"PRUEBA: '{input_str}'")
    print("="*30)
    
    input_stream = InputStream(input_str)
    
    # Lexer
    lexer = PrintLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    print("\nTOKENS GENERADOS:")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = PrintParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    # Parser
    parser = PrintParser(token_stream)
    tree = parser.stat()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["print x", "print 5"]
    for i in inputs:
        test(i)

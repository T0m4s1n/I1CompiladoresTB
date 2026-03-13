from antlr4 import *
from MiniLexer import MiniLexer
from MiniParser import MiniParser

def test(input_str):
    print(f"\n" + "="*30)
    print(f"PRUEBA:\n{input_str}")
    print("="*30)
    
    input_stream = InputStream(input_str)
    
    # Lexer
    lexer = MiniLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    print("\nTOKENS GENERADOS:")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = MiniParser.symbolicNames[token.type]
            print(f"Texto: {repr(token.text):<10} Tipo: {token_name}")
    
    # Parser
    parser = MiniParser(token_stream)
    tree = parser.prog()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["x = 5\ny = 10\nprint x\nprint y"]
    for i in inputs:
        test(i)

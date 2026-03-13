from antlr4 import *
from IdentificadorLexer import IdentificadorLexer
from IdentificadorParser import IdentificadorParser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = IdentificadorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = IdentificadorParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = IdentificadorParser(token_stream)
    tree = parser.id_()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["x", "variable", "contador", "valor1"]
    for i in inputs:
        test(i)

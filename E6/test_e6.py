from antlr4 import *
from Saludo2Lexer import Saludo2Lexer
from Saludo2Parser import Saludo2Parser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = Saludo2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = Saludo2Parser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = Saludo2Parser(token_stream)
    tree = parser.saludo()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["hola Juan", "buenosdias Pedro"]
    for i in inputs:
        test(i)

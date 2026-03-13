from antlr4 import *
from ListaComasLexer import ListaComasLexer
from ListaComasParser import ListaComasParser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = ListaComasLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = ListaComasParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = ListaComasParser(token_stream)
    tree = parser.lista()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["1,2,3", "5,10,15"]
    for i in inputs:
        test(i)

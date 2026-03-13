from antlr4 import *
from Expr3Lexer import Expr3Lexer
from Expr3Parser import Expr3Parser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = Expr3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = Expr3Parser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = Expr3Parser(token_stream)
    tree = parser.expr()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["3+4*5"]
    for i in inputs:
        test(i)

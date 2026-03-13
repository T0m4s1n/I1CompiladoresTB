from antlr4 import *
from Expr1Lexer import Expr1Lexer
from Expr1Parser import Expr1Parser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = Expr1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = Expr1Parser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = Expr1Parser(token_stream)
    tree = parser.expr()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["1+2+3", "5+6+7+8"]
    for i in inputs:
        test(i)

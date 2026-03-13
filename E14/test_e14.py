from antlr4 import *
from ParentesisLexer import ParentesisLexer
from ParentesisParser import ParentesisParser

def test(input_str):
    print(f"PRUEBA: '{input_str}'")
    
    input_stream = InputStream(input_str)
    
    lexer = ParentesisLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = ParentesisParser.symbolicNames[token.type]
            print(f"Texto: {token.text:<10} Tipo: {token_name}")
    
    parser = ParentesisParser(token_stream)
    tree = parser.expr()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["(3+4)*5"]
    for i in inputs:
        test(i)

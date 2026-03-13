from antlr4 import *
from ProgramaLexer import ProgramaLexer
from ProgramaParser import ProgramaParser

def test(input_str):
    print(f"PRUEBA:\n{input_str}")
    
    input_stream = InputStream(input_str)
    
    lexer = ProgramaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = ProgramaParser.symbolicNames[token.type]
            print(f"Texto: {repr(token.text):<10} Tipo: {token_name}")
    
    parser = ProgramaParser(token_stream)
    tree = parser.prog()
    
    print("\nÁRBOL SINTÁCTICO:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    inputs = ["x=5\ny=10\nz=20"]
    for i in inputs:
        test(i)

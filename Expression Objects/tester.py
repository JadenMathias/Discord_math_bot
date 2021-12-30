from lexer import Lexer
from processor import Parser
text = ""
while text != "stop":
    text = input("Enter expression: ")
    lexer = Lexer(text)
    elements = lexer.generate_elements()
    parser = Parser(elements)
    x = parser.parse()
    print("Expression:", x)
    x = x.derivate()
    while x != x.simplify():
        x = x.simplify()
    print("Derivative:", x)

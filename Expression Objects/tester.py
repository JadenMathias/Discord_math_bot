from lexer import Lexer
text = ""
while text != "stop":
    text = input("Enter expression: ")
    lexer = Lexer(text)
    elements = lexer.generate_elements()
    print(list(elements))

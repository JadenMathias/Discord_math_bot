from processor import Processor
t1 = ""
while t1 != "stop":
    t1 = input("Enter expression: ")
    if t1 == "stop": continue
    t2 = input("Enter variable to derivate wrt: ")

    parser = Processor()
    x = parser.parse(t1)
    y = parser.parse(t2)

    print("Expression:", x)
    x = x.derivate(y)
    while x != x.simplify():
        x = x.simplify()
    print("Derivative:", x)

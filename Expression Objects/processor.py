"""
    This module will convert Elements to a expression tree.
    Tree precedence is determined via the BEDMAS rule.
    Brackets                -> ( | ) | Variables | Constants | Trigonometric | Logarithmetic
    Exponents               -> ^
    Division/Multiplication -> * | /
    Addition/Subtraction    -> + | -
"""

from elements import ElementType
from expression import *
import lexer

AS = (ElementType.ADD, ElementType.SUB)
PD = (ElementType.PROD, ElementType.DIV)

"""Class Processor Method:

   - parse(text)
     Converts a string expression 'text' to a Expression tree via the lexer
"""

class Processor:

    def __init__(self):

        self.elements = None
        
    
    def advance(self):
        try:
            self.element = next(self.elements) # goes to next element
        except StopIteration:
            self.element = None

    """The parse method uses submethods below it to traverse the Elements of the string retrived by the
       lexer to return the string in a Expression tree format."""
    def parse(self,text):

        elements = lexer.Lexer(text).generate_elements()
        self.elements = iter(elements)
        self.advance() #intialize to first element of lexer output

        if self.element == None:
            return None #Null if no elements retrieved from lexer
            
        expression = self.AddSub() #Final expression

        if self.element != None: 
            raise Exception("Invalid expression") 
            #Tree is Invalid if there are still elements to obtain after assigning the expression

        return expression

    """Add/Sub is of the form (ProdDiv() +- ProdDiv())"""
    def AddSub(self):

        # We called ProdDiv() first as it has higher precedence than AddSub()
        result = self.ProdDiv()

        # After obtaining the above we check if the current element is a Add or Sub
        #to form the Add/Sub node
        while self.element != None and self.element.type in AS:
            # Result holds the LHS of Add/Sub and ProdDiv() will retrieve the RHS
            #Again note that RHS is of higher precedence so we call ProdDiv() to
            #Find it
            if self.element.type == ElementType.ADD:
                self.advance()
                result = Add(result , self.ProdDiv()) 
            elif self.element.type == ElementType.SUB:
                self.advance()
                result = Sub(result ,self.ProdDiv())
        
        return result

    """Prod/Div is of the form (Power() */ Power())"""
    def ProdDiv(self):

        #Similar Logic as Above.
        result = self.Power()

        while self.element != None and self.element.type in PD:
            if self.element.type == ElementType.PROD:
                self.advance()
                result = Multi(result ,self.Power())
            elif self.element.type == ElementType.DIV:
                self.advance()
                result = Div(result ,self.Power())
        
        return result

    """Power is of the form (Brac() ^ Brac())"""
    def Power(self):

        #Similar Logic as Above.
        result = self.Brac()

        while  self.element != None and self.element.type  == ElementType.EXP:
            if self.element.type == ElementType.EXP:
                self.advance()
                result = Exponent(result ,self.Brac())

        
        return result
    
    """Handles Highest precedence elements"""
    def Brac(self):

        # We finally return the highest precedence elements to the
        #preceding function which return it back to its preceding function.
        #this happens in order of precedence (high -> low)
        e = self.element

        if e.type == ElementType.LP:
            # If we come across a '(' we check for a new expression inside.
            self.advance()
            result = self.AddSub()
            # After we get the expression we check if the current element is a
            #')' to ensure validity
            if self.element.type != ElementType.RP:
                raise Exception ("Invalid Expression")
            self.advance()
            return result
        #All the trig elements below are followed by a '('
        #Thus we call the Brac() as its inner argument.
        elif e.type == ElementType.SIN:
            self.advance()
            return Sin(self.Brac())
        elif e.type == ElementType.COS:
            self.advance()
            return Cos(self.Brac())
        elif e.type == ElementType.TAN:
            self.advance()
            return Tan(self.Brac())
        elif e.type == ElementType.SEC:
            self.advance()
            return Sec(self.Brac())
        elif e.type == ElementType.COSEC:
            self.advance()
            return Cosec(self.Brac())
        elif e.type == ElementType.COT:
            self.advance()
            return Cot(self.Brac())
        elif e.type == ElementType.LOG:
            self.advance()
            return Log(self.Brac())
        elif e.type == ElementType.CONSTANT:
            self.advance()
            return Constant(e.value)
        elif e.type == ElementType.PI:
            self.advance()
            return pi()
        elif e.type == ElementType.E:
            self.advance()
            return Euler()
        elif e.type == ElementType.VAR:
            self.advance()
            return Variable(e.value)
        elif e.type == ElementType.ADD:
            self.advance()
            return uPlus(self.Brac())
        elif e.type == ElementType.SUB:
            self.advance()
            return uMinus(self.Brac())
        else:
            raise Exception("Invalid expression")




    
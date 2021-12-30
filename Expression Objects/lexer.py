from elements import *

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
VTL = { 'sin' : Element(ElementType.SIN), 'cos'   : Element(ElementType.COS),  'tan' : Element(ElementType.TAN),
        'sec' : Element(ElementType.SEC), 'cosec' : Element(ElementType.COSEC),'cot' : Element(ElementType.COT),
        'pi'  : Element(ElementType.PI),  'e'     : Element(ElementType.E),    'log' : Element(ElementType.LOG) }

class Lexer:
    
    def __init__(self,text):
        
        self.text = iter(text)
        self.advance()
    
    def advance(self):

       try:
           self.char = next(self.text)
       except StopIteration:
           self.char = None
    
        
    def generate_elements(self):

        while self.char != None:
            if self.char in WHITESPACE:
                self.advance()
            elif self.char.isalpha():
                yield self.generate_vtl()
            elif self.char in DIGITS or self.char == '.':
                yield self.generate_number()
            elif self.char == '+':
                self.advance()
                yield Element(ElementType.ADD)
            elif self.char == '-':
                self.advance()
                yield Element(ElementType.SUB)
            elif self.char == '*':
                self.advance()
                yield Element(ElementType.PROD)
            elif self.char == '/':
                self.advance()
                yield Element(ElementType.DIV)
            elif self.char == '^':
                self.advance()
                yield Element(ElementType.EXP)
            elif self.char == '(':
                self.advance()
                yield Element(ElementType.LP)
            elif self.char == ')':
                self.advance()
                yield Element(ElementType.RP)
            else:
                raise Exception(f"Illegal Character: '{self.char}'")
      
    def generate_vtl(self):

        string = self.char
        self.advance()

        while self.char != None and self.char.isalpha():
            string = string + self.char
            self.advance()

        for k in VTL:
            if string == k:
                return VTL[k]
        else:
            return Element(ElementType.VAR, string)

    def generate_number(self):
        
        decimal_count = 0
        number_str = self.char
        self.advance()
        
        while self.char != None and (self.char == "." or self.char in DIGITS):
            if self.char == '.':
                decimal_count += 1
                if decimal_count > 1:
                    break
            
            number_str += self.char
            self.advance() 

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Element(ElementType.CONSTANT , float(number_str))

        
        

   

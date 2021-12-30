"""
The purpose of this module is to read a arithmetic expression of type string and
seperate its elements and return a list of Elements
"""

from elements import *


WHITESPACE = ' \n\t'  #White Space characters
DIGITS = '0123456789' #Possible Digits of a number

# VTL (Variable | Trigonometric | Logarithmic) is a dictionary of possible math functions 
# we can expect from the string and its Element type
VTL = { 'sin' : Element(ElementType.SIN), 'cos'   : Element(ElementType.COS),  'tan' : Element(ElementType.TAN),
        'sec' : Element(ElementType.SEC), 'cosec' : Element(ElementType.COSEC),'cot' : Element(ElementType.COT),
        'pi'  : Element(ElementType.PI),  'e'     : Element(ElementType.E),    'log' : Element(ElementType.LOG) }

class Lexer:
    
    """Construct a lexer that takes some Math expression text and stores it as a iterator."""
    def __init__(self,text):
        
        #Calls the advance method which iterates to the first element of the text.
        #The generate_elements() method will yield the elements from the expression.

        self.text = iter(text)
        self.advance()
    
    """Go to the next element of the expression, exception when we reach the end: return None."""
    def advance(self):

       try:
           self.char = next(self.text)
       except StopIteration:
           self.char = None
    
    """lexing function converts the expression to Elements."""
    def generate_elements(self):

        while self.char != None:
            if self.char in WHITESPACE:
                #Ignore all whitespaces in a expression and advance
                self.advance()
            elif self.char.isalpha():
                #If we come across a alphabet, call the generate_vtl method
                yield self.generate_vtl()
            elif self.char in DIGITS or self.char == '.':
                #If we come across a digit or decimal, call the generate_number method
                yield self.generate_number()
            #If we come across any operator, append yield the respective Element:
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
    
    """Function generates a VTL from the expression based on the fact that VTL starts with a alphabet."""
    def generate_vtl(self):
        
        #Intializes 'string' as the current character and goes next
        string = self.char 
        self.advance()     

        #Since we found a alphabet we check and append the next characters to 'string' if they are alphabets
        while self.char != None and self.char.isalpha():
            string = string + self.char
            self.advance()

        #check if the string matches a key in VTL and return the matching keys value as the Element.
        #Else returns the string as a Variable element
        for k in VTL:
            if string == k:
                return VTL[k]
        else:
            return Element(ElementType.VAR, string)

    """Similar to generate_vtl except we form a float number in this case."""
    def generate_number(self):
        
        #We keep track of decimals to ensure a number has a single deicmal point.
        decimal_count = 0
        number_str = self.char
        self.advance()
        
        #append the next characters as long as it is a digit or float and decimal count isnt more than 1.
        while self.char != None and (self.char == "." or self.char in DIGITS):
            if self.char == '.':
                decimal_count += 1
                if decimal_count > 1:
                    break
            
            number_str += self.char
            self.advance() 

        #Adjust the resulting number_str if a decimal is at the beginning or end to form a valid float.
        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        #Return Number Element with the float of number_str as its value.
        return Element(ElementType.CONSTANT , float(number_str))

        
        

   

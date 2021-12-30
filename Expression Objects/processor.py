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

AS = (ElementType.ADD, ElementType.SUB)
PD = (ElementType.PROD, ElementType.DIV)

#TODO: Brief comments!

class Parser:

    def __init__(self, elements):
        self.elements = iter(elements)
        self.advance()
    
    def advance(self):
        try:
            self.element = next(self.elements)
        except StopIteration:
            self.element = None
    
    def parse(self):
        if self.element == None:
            return None
            
        expression = self.AddSub()

        if self.element != None:
            raise Exception("Invalid expression")

        return expression

    def AddSub(self):
        result = self.ProdDiv()

        while self.element != None and self.element.type in AS:
            if self.element.type == ElementType.ADD:
                self.advance()
                result = Add(result ,self.ProdDiv())
            elif self.element.type == ElementType.SUB:
                self.advance()
                result = Sub(result ,self.ProdDiv())
        
        return result

    def ProdDiv(self):
        result = self.Power()

        while self.element != None and self.element.type in PD:
            if self.element.type == ElementType.PROD:
                self.advance()
                result = Multi(result ,self.Power())
            elif self.element.type == ElementType.DIV:
                self.advance()
                result = Div(result ,self.Power())
        
        return result


    def Power(self):
        result = self.Brac()

        while  self.element != None and self.element.type  == ElementType.EXP:
            if self.element.type == ElementType.EXP:
                self.advance()
                result = Exponent(result ,self.Brac())

        
        return result
    
    def Brac(self):
        e = self.element

        if e.type == ElementType.LP:
            self.advance()
            result = self.AddSub()
            if self.element.type != ElementType.RP:
                raise Exception ("Invalid Expression")
            self.advance()
            return result
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




    
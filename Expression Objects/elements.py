"""
Elements.py is a module that defines a type for every term that can be found in a mathematical expression.

These types will be used to represent arithmetic expression terms in a string in a more parsable format.
"""

from enum import Enum
from dataclasses import dataclass


"""The Enum library is used to declare the possible ElementTypes"""
class ElementType(Enum):
    VAR      = 0  # Math variables like 'x'
    CONSTANT = 1  # Math numbers        '0'
    PI       = 2  # Special constant pi 'pi'
    E        = 3  # Special constant e  'e'
    SIN      = 4  # Trig function 'sin'
    COS      = 5  # Trig function 'cos'
    TAN      = 6  # Trig function 'tan'
    SEC      = 7  # Trig function 'sec'
    COSEC    = 8  # Trig function 'cosec'
    COT      = 9  # Trig function 'cot'
    LOG      = 10 # Trig function 'log'
    ADD      = 11 # Binary operator '+'
    SUB      = 12 # Binary operator '-'
    PROD     = 13 # Binary operator '*'
    DIV      = 14 # Binary operator '/'
    EXP      = 15 # Binary operator '^'
    LP       = 16 # '('
    RP       = 17 # ')'

"""An Element object can be any of the Above types, some may hold a value (like constants)"""
@dataclass
class Element:

    type : ElementType 
    value: any = None

    def __repr__(self):
        return f"{self.type.name}: {self.value}"

"""
    This module will convert Elements to a expression tree.
    Tree precedence is determined via the BEDMAS rule.
    Brackets                -> ( | ) | Variables | Constants
    Exponents               -> ^
    Division/Multiplication -> * | /
    Addition/Subtraction    -> + | -
"""


from elements import *
from expression import *

class parser:

    def __init__(self, eList) -> None:
        pass
    
    
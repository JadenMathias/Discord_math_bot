from enum import Enum
from dataclasses import dataclass

class ElementType(Enum):
    VAR      = 0  # 'x'
    CONSTANT = 1  # '0'
    PI       = 2  # 'pi'
    E        = 3  # 'e'
    SIN      = 4  # 'sin'
    COS      = 5  # 'cos'
    TAN      = 6  # 'tan'
    SEC      = 7  # 'sec'
    COSEC    = 8  # 'cosec'
    COT      = 9  # 'cot'
    LOG      = 10 # 'log'
    ADD      = 11 # '+'
    SUB      = 12 # '-'
    PROD     = 13 # '*'
    DIV      = 14 # '/'
    EXP      = 15 # '^'
    LP       = 16 # '('
    RP       = 17 # ')'

@dataclass
class Element:
    type :  ElementType
    value: any = None
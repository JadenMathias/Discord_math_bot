from enum import Enum
from dataclasses import dataclass

class ElementType(Enum):
    VAR      = 0
    CONSTANT = 1
    PI       = 2
    E        = 3
    SIN      = 4
    COS      = 5
    TAN      = 6
    SEC      = 7
    COSEC    = 8
    COT      = 9
    LOG      = 10
    ADD      = 11
    SUB      = 12
    PROD     = 13
    DIV      = 14
    EXP      = 15
    LP       = 16
    RP       = 17

@dataclass
class Element:
    type:  ElementType
    value: any = None
"""
    This module describes properties for each math expression element, we use these 
    objects to represent our Elements to perform more complex arithmetic functions.

    currently supports: 

    1. Derivatives
     - Each expression has a derivate() method, following the basic 
       rules of differentiation.

    2. Simplification:
     - Each expression has a simplify() method, following basic rules
       of arithmetic simplification()
    
    3. Representation:
     - Each expression has a readable arithmetic representation via the
       __repr__() methods
"""


import math
from dataclasses import dataclass

#TODO: Implement variable substituition and expression evaluation

#--------------- Variable  ---------------- #

@dataclass
class Variable:

    value : str = 'x'

    def derivate(self, x):
        if self.value == x.value:
            return Constant(1)
        else:
            return Derivable(Variable(x.value), self)

    def substitute(self, x : str, y):
        if self.value == x:
            return y
        else:
            return self
    
    def simplify(self):
        return self
    
    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value

# Represents variable meant to be derivated
#TODO : Complete Derivable 'dy/dx'
@dataclass
class Derivable:
    
    dy : Variable = Variable('y')
    dx : Variable = Variable()

    def derivate(self, x = Variable()):
        pass
        #return Derivable(self,x)

    def substitute(self, x : str, y):
        pass
        #if self.value == x:
        #    return y.derivate()
        #else:
        #    return self

    def simplify(self):
        return self

    def __repr__(self):
        return self.dy.value + "'"
        
    def __str__(self):
        return self.dy.value + "'"

#TODO: Implement Substitute methods for every expression
#--------------- Constants ---------------- #
@dataclass
class Constant:
    
    value : float = 0.0
    
    def derivate(self, x = Variable()):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return f"{self.value}"
    
    def __str__(self):
        return f"{self.value}"

@dataclass     
class Euler:

    value : float = math.e
    
    def derivate(self, x = Variable()):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return "e"
    
    def __str__(self):
        return "e"

@dataclass
class pi:

    value : float = math.pi
    
    def derivate(self, x = Variable()):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return "pi"
    
    def __str__(self):
        return "pi"

#--------------- Operators ---------------- #
@dataclass
class uMinus:

    X: any

    def simplify(self):
        if self.X == Constant(0):
            return Constant(0)

        return uMinus(self.X.simplify())
    
    def derivate(self, x = Variable()):
        return uMinus(self.X.derivate(x))
    
    def __repr__(self):
        return f"-{self.X}"
        
    def __str__(self):
        return f"-{self.X}"

@dataclass
class Add:
    
    L: any
    R: any
    
    def simplify(self):
        if self.L == Constant(0):
            return self.R.simplify()
        elif self.R == Constant(0):
            return self.L.simplify()
        
        try:
            if self.R == uMinus(self.R.X):
                return Sub(self.L.simplify(), self.R.X.simplify())
            elif self.L == uMinus(self.L.X):
                return Sub(self.R.simplify(), self.L.X.simplify())
        except:
            pass

        return Add(self.L.simplify(),self.R.simplify())

    def derivate(self, x = Variable()):
        return (Add(self.L.derivate(x), self.R.derivate(x)))
    
    def __repr__(self):
        return f"({self.L} + {self.R})"
    
    def __str__(self):
        return f"({self.L} + {self.R})"
        
@dataclass
class Sub:
    
    L: any
    R: any

    def simplify(self):
        if self.L == Constant(0):
            return uMinus(self.R.simplify())
        elif self.R == Constant(0):
            return self.L.simplify()

        return Sub(self.L.simplify(),self.R.simplify())

    def derivate(self, x = Variable()):
        return Sub(self.L.derivate(x), self.R.derivate(x))
    
    def __repr__(self):
        return f"({self.L} - {self.R})"
    
    def __str__(self):
        return f"({self.L} - {self.R})"

@dataclass       
class Multi:
    
    L: any
    R: any
    
    def simplify(self):
        if self.L == Constant(0) or self.R == Constant(0):
            return Constant(0)
        elif self.L == Constant(1):
            return self.R.simplify()
        elif self.R == Constant(1):
            return self.L.simplify()

        return Multi(self.L.simplify(),self.R.simplify())

    def derivate(self, x = Variable()):
        return Add(Multi(self.L, self.R.derivate(x)), Multi(self.R, self.L.derivate(x)))
    
    def __repr__(self):
        return f"({self.L} * {self.R})"
    
    def __str__(self):
        return f"({self.L} * {self.R})"

@dataclass
class Div:
       
    U: any
    V: any
    
    def simplify(self):
        if self.U == Constant(0):
            return Constant(0)
        elif self.V == Constant(1):
            return self.U.simplify()
        
        return Div(self.U.simplify(),self.V.simplify())

    def derivate(self, x = Variable()):
        return Div(Sub(Multi(self.V,self.U.derivate(x)),Multi(self.U,self.V.derivate(x))),Exponent(self.V,Constant(2)))
    
    def __repr__(self):
        return f"({self.U} / {self.V})"

    def __str__(self):
        return f"({self.U} / {self.V})"

@dataclass
class Exponent:

    U: any
    V: any

    def simplify(self):
        if self.U == Constant(0):
            return Constant(0)
        elif self.V == Constant(0):
            return Constant(1)
        elif self.U == Constant(1):
            return Constant(1)
        elif self.V == Constant(1):
            return self.U.simplify()
        return Exponent(self.U.simplify(),self.V.simplify())
    
    def derivate(self, x = Variable()):
        g = (Multi(self.V, Log(self.U))).derivate(x)
        return Multi(Exponent(self.U,self.V), g)
    
    def __repr__(self):
        return f"({self.U} ^ {self.V})"

    def __str__(self):
        return f"({self.U} ^ {self.V})"


@dataclass
class uPlus:

    X: any
    
    def simplify(self):
        if self.X == Constant(0):
            return Constant(0)
            
        return uPlus(self.X.simplify())
    
    def derivate(self, x = Variable()):
        return uPlus(self.X.derivate(x))
    
    def __repr__(self):
        return f"+{self.X}"

    def __str__(self):
        return f"+{self.X}"


#--------------- Trigonometry ---------------- #

@dataclass
class Sin:
    
    X: any

    def simplify(self):
        return Sin(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(Cos(self.X), self.X.derivate(x))
    
    def __repr__(self):
        return f"sin({self.X})"

    def __str__(self):
        return f"sin({self.X})"

@dataclass
class Tan:
    
    X: any
    
    def simplify(self):
        return Tan(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(Exponent(Sec(self.X), Constant(2)), self.X.derivate(x))

    def __repr__(self):
        return f"tan({self.X})"
    
    def __str__(self):
        return f"tan({self.X})"

@dataclass
class Sec:
    
    X: any
        
    def simplify(self):
        return Sec(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(Multi(Sec(self.X), Tan(self.X)), self.X.derivate(x))
    
    def __repr__(self):
        return f"sec({self.X})"
    
    def __str__(self):
        return f"sec({self.X})"


@dataclass
class Cos:
    
    X: any
    
    def simplify(self):
        return Cos(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(uMinus(Sin(self.X)), self.X.derivate(x))
    
    def __repr__(self):
        return f"cos({self.X})"

    def __str__(self):
        return f"cos({self.X})"

@dataclass
class Cot:
    
    X: any

    def simplify(self):
        return Cot(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(uMinus(Exponent(Sec(self.X), Constant(2))), self.X.derivate(x))
    
    def __repr__(self):
        return f"cot({self.X})"

    def __str__(self):
        return f"cot({self.X})"

@dataclass
class Cosec:
    
    X: any

    def simplify(self):
        return Cosec(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(uMinus(Multi(Cosec(self.X), Cot(self.X))), self.X.derivate(x))
    
    def __repr__(self):
        return f"cosec({self.X})"

    def __str__(self):
        return f"cosec({self.X})"

@dataclass
class Log:

    X: any

    def simplify(self):
        return Log(self.X.simplify())

    def derivate(self, x = Variable()):
        return Multi(Div(Constant(1),self.X), self.X.derivate(x))

    def __repr__(self):
        return f"ln({self.X})"

    def __str__(self):
        return f"ln({self.X})"


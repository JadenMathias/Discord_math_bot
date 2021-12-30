import math
from dataclasses import dataclass

#--------------- Variable  ---------------- #

@dataclass
class Variable:

    value : str = 'x'

    def derivate(self, x : str = 'x'):
        if self.value == x:
            return Constant(1)
        else:
            return Variable(self.value+"'")
    
    def simplify(self):
        return self
    
    def __repr__(self):
        return self.value

#--------------- Constants ---------------- #
@dataclass
class Constant:
    
    value : float
    
    def derivate(self, x : str = 'x'):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return f"{self.value}"

@dataclass     
class e:

    value : float = math.e
    
    def derivate(self, x : str = 'x'):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return f"{self.value}"

@dataclass
class pi:

    value : float = math.pi
    
    def derivate(self, x : str = 'x'):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return f"{self.value}"

#--------------- Operators ---------------- #

@dataclass
class Add:
    
    L: any
    R: any

    def __repr__(self):
        return f"({self.L} + {self.R})"
    
    def simplify(self):
        if self.L == Constant(0):
            return self.R.simplify()
        elif self.R == Constant(0):
            return self.L.simplify()

        return Add(self.L.simplify(),self.R.simplify())

    def derivate(self, x : str = 'x'):
        return (Add(self.L.derivate(x), self.R.derivate(x)))

        
@dataclass
class Sub:
    
    L: any
    R: any

    def __repr__(self):
        return f"({self.L} - {self.R})"

    def simplify(self):
        if self.L == Constant(0):
            return uMinus(self.R.simplify())
        elif self.R == Constant(0):
            return self.L.simplify()

        return Sub(self.L.simplify(),self.R.simplify())

    def derivate(self, x : str = 'x'):
        return Sub(self.L.derivate(x), self.R.derivate(x))

@dataclass       
class Multi:
    
    L: any
    R: any

    def __repr__(self):
        return f"({self.L} * {self.R})"
    
    def simplify(self):
        if self.L == Constant(0) or self.R == Constant(0):
            return Constant(0)
        elif self.L == Constant(1):
            return self.R.simplify()
        elif self.R == Constant(1):
            return self.L.simplify()

        return Multi(self.L.simplify(),self.R.simplify())

    def derivate(self, x : str = 'x'):
        return Add(Multi(self.L, self.R.derivate(x)), Multi(self.R, self.L.derivate(x)))

@dataclass
class Div:
       
    U: any
    V: any

    def __repr__(self):
        return f"({self.U} / {self.V})"
    
    def simplify(self):
        if self.U == Constant(0):
            return Constant(0)
        elif self.V == Constant(1):
            return self.U.simplify()
        
        return Div(self.U.simplify(),self.V.simplify())

    def derivate(self, x : str = 'x'):
        return Div(Sub(Multi(self.V,self.U.derivate(x)),Multi(self.U,self.V.derivate(x))),Exponent(self.V,Constant(2)))

@dataclass
class Exponent:

    U: any
    V: any

    def __repr__(self):
        return f"({self.U} ^ {self.V})"

    
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

    def derivate(self, x : str = 'x'):
        return Multi(self,Multi(self.U, Log(self.v)).derivate(x))

@dataclass
class uMinus:

    X: any
    
    def __repr__(self):
        return f"-{self.X}"

    def simplify(self):
        if self.X == Constant(0):
            return Constant(0)

        return uMinus(self.X.simplify())
    
    def derivate(self, x : str = 'x'):
        return uMinus(self.X.derivate(x))

@dataclass
class uPlus:

    X: any
    
    def __repr__(self):
        return f"+{self.X}"
    
    def simplify(self):
        if self.X == Constant(0):
            return Constant(0)
            
        return uPlus(self.X.simplify())
    
    def derivate(self, x : str = 'x'):
        return uPlus(self.X.derivate(x))


#--------------- Trigonometry ---------------- #

@dataclass
class Sin:
    
    X: any

    def __repr__(self):
        return f"sin({self.X})"

    def simplify(self):
        return Sin(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(Cos(self.X), self.X.derivate(x))

@dataclass
class Tan:
    
    X: any

    def __repr__(self):
        return f"tan({self.X})"
    
    def simplify(self):
        return Tan(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(Exponent(Sec(self.X), Constant(2)), self.X.derivate(x))

@dataclass
class Sec:
    
    X: any

    def __repr__(self):
        return f"sec({self.X})"
    
    def simplify(self):
        return Sec(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(Multi(Sec(self.X), Tan(self.X)), self.X.derivate(x))


@dataclass
class Cos:
    
    X: any

    def __repr__(self):
        return f"cos({self.X})"
    
    def simplify(self):
        return Cos(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(uMinus(Sin(self.X)), self.X.derivate(x))

@dataclass
class Cot:
    
    X: any

    def __repr__(self):
        return f"cot({self.X})"

    def simplify(self):
        return Cot(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(uMinus(Exponent(Sec(self.X), Constant(2))), self.X.derivate(x))

@dataclass
class Cosec:
    
    X: any

    def __repr__(self):
        return f"cosec({self.X})"

    def simplify(self):
        return Cosec(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(uMinus(Multi(Cosec(self.X), Cot(self.X))), self.X.derivate(x))

@dataclass
class Log:

    X: any

    def __repr__(self):
        return f"ln({self.X})"

    def simplify(self):
        return Log(self.X.simplify())

    def derivate(self, x : str = 'x'):
        return Multi(Div(Constant(1),self.X), self.X.derivate(x))


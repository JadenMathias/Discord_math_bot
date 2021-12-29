import math
from dataclasses import dataclass

#--------------- Constants ---------------- #
@dataclass
class Constant:
    
    value : float
    
    def derivate(self):
        return Constant(0)

    def __repr__(self):
        return f"{self.value}"

@dataclass     
class e:

    value : float = math.e
    
    def derivate(self):
        return Constant(0)

    def __repr__(self):
        return f"{self.value}"

@dataclass
class pi:

    value : float = math.pi
    
    def derivate(self):
        return Constant(0)

    def __repr__(self):
        return f"{self.value}"

#--------------- Operators ---------------- #

@dataclass
class Add:
    
    L: any
    R: any

    def __repr__(self):
        return f"({self.L} + {self.R})"
    
    def derivate(self):
        return (Add(self.L.derivate(), self.R.derivate()))

        
@dataclass
class Sub:
    
    L: any
    R: any

    def __repr__(self):
        return f"({self.L} - {self.R})"

    def derivate(self):
        return Sub(self.L.derivate(), self.R.derivate())

@dataclass       
class Multi:
    
    L: any
    R: any

    def __repr__(self):
        return f"({self.L} * {self.R})"

    def derivate(self):
        return Add(Multi(self.U, self.V.derivate()), Multi(self.V, self.U.derivate()))

# U / V = div(U, V)
@dataclass
class Div:
       
    U: any
    V: any

    def __repr__(self):
        return f"({self.U} / {self.V})"

    def derivate(self):
        return Div(Sub(Multi(self.V,self.U.derivate()),Multi(self.U,self.V.derivate())),Exponent(self.V,Constant(2)))

# U ^ V
@dataclass
class Exponent:

    U: any
    V: any

    def __repr__(self):
        return f"({self.U} ^ {self.R})"

    
    def derivate():
        pass


#--------------- Trigonometry ---------------- #

@dataclass
class Sin:
    
    X: any

    def __repr__(self):
        return f"sin({self.X})"

    def derivate(self):
        return Multi(Cos(self.X), self.X.derivate())

@dataclass
class Tan:
    
    X: any

    def __repr__(self):
        return f"tan({self.X})"

    def derivate(self):
        return Multi(Exponent(Sec(self.X), Constant(2)), self.X.derivate())

@dataclass
class Sec:
    
    X: any

    def __repr__(self):
        return f"sec({self.X})"

    def derivate(self):
        return Multi(Multi(Sec(self.X), Tan(self.X)), self.X.derivate())

#TODO: Add Unary minus to the below derivate functions

@dataclass
class Cos:
    
    X: any

    def __repr__(self):
        return f"cos({self.X})"

    def derivate(self):
        return Multi(Sin(self.X), self.X.derivate())

@dataclass
class Cot:
    
    X: any

    def __repr__(self):
        return f"cot({self.X})"

    def derivate(self):
        return Multi(Exponent(Sec(self.X), Constant(2)), self.X.derivate())

@dataclass
class Cosec:
    
    X: any

    def __repr__(self):
        return f"cosec({self.X})"

    def derivate(self):
        return Multi(Multi(Cosec(self.X), Cot(self.X)), self.X.derivate())

#TODO: Unary operator nodes

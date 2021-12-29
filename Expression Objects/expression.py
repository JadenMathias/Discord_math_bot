import math
from dataclasses import dataclass

#--------------- Constants ---------------- #
class Constant:
    
    def __init__(self, X):
        self.value = X
    
    def derivate():
        return Constant(0)
            
class e:

    def __init__(self):
        self.value = math.e

class pi:

    def __init__(self):
        self.value = math.pi

#--------------- Operators ---------------- #
class Add:
    
    def __init__(self, L, R):
        self.L = L
        self.R = R

    def derivate(self):
        return (Add(self.L.derivate(), self.R.derivate()))
        

class Sub:
    
    def __init__(self, L, R):
        self.L = L
        self.R = R

    def derivate(self):
        return Sub(self.L.derivate(),self.R.derivate())
        
class Multi:
    
    def __init__(self, U, V, sign = 1):
        self.u = U
        self.v = V
        self.sign = sign

    def derivate(self):
        return Add(Multi(self.U, self.V.derivate()), Multi(self.V, self.U.derivate()))

# U / V = div(U, V)
class Div:
       
    def __init__(self, U, V):
        self.u = U
        self.v = V

    def derivate(self):
        return Div(Sub(Multi(self.V,self.U.derivate()),Multi(self.U,self.V.derivate())),Exponent(self.V,Constant(2)))

# U ^ V
class Exponent:

    def __init__(self,U,V):
        self.u=U
        self.v=V
    
    def derivate():
        pass


#--------------- Trigonometry ---------------- #
class Sin:
    
    def __init__(self, X, sign = 1):
        self.X = X
        self.sign = sign

    def derivate(self):
        return Multi(Cos(self.X), self.X.derivate(), self.sign)

class Tan:
    
    def __init__(self, X, sign = 1):
        self.X = X
        self.sign = sign

    def derivate(self):
        return Multi(Exponent(Sec(self.X), Constant(2)), self.X.derivate(), self.sign)

class Sec:
    
    def __init__(self, X, sign = 1):
        self.X = X
        self.sign = sign

    def derivate(self):
        return Multi(Multi(Sec(self.X), Tan(self.X) , self.sign), self.X.derivate())

class Cos:
    
    def __init__(self, X, sign):
        self.X = X
        self.sign = sign

    def derivate(self):
        return Multi(Sin(self.X), self.X.derivate(), self.sign * -1)

class Cot:
    
    def __init__(self, X, sign = 1):
        self.X = X
        self.sign = sign

    def derivate(self):
        return Multi(Exponent(Sec(self.X), Constant(2) , self.sign * -1), self.X.derivate())

class Cosec:
    
    def __init__(self, X, sign = 1):
        self.X = X
        self.sign = sign

    def derivate(self):
        return Multi(Multi(Cosec(self.X), Cot(self.X) , self.sign * -1), self.X.derivate())
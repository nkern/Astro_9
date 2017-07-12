import math

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i
        self.abs = math.sqrt(r**2 + i**2)
    
    def __repr__(self):
        return "(%s, %sj)" % (self.real, self.imag)
        
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)
        
    def conjugate(self):
        return Complex(self.real, -self.imag)

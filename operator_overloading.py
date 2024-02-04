class operator_overloading:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    def __mod__(self,other):
        return self.a%other.a
    def __pow__(self,other):
        return self.a**other.a
    def __eq__(self,other):
        return self.a == other.a
    def __ne__ (self,other):
        return self.a != other.a
    def __gt__(self,other):
        return self.a > other.a
    def __lt__(self,other):
        return self.a < other.a
    def __ge__(self,other):
        return self.a >= other.a
    def __le__(self,other):
        return self.a <= other.a
    def __or__(self,other):
        return self.a | other.a
    def __and__(self,other):
        return self.a & other.a
    def __xor__(self,other):
        return self.a ^ other.a
    def __invert__(self):
        return ~ self.a
    def __invert__(other):
        return ~ other.a
    def __lshift__(self,other):
        return self.a <<  other.a
    def __rshift__ (self,other):
        return self.a >> other.a

s1=operator_overloading(10)
s2=operator_overloading(20)

    
    

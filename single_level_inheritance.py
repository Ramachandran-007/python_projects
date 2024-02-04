class A:
    a=1
    def __init__(self,c):
        self.c=c
    def a_display(self):
        print(self.c)
        print('Class A')

class B(A):
    b=12
    def __init__(self,c,d,e):
        super().__init__(c)
        self.d=d
        self.e=e

    def display(self):
        super().a_display()
        print(self.d)
        print(self.e)

ob=A(11)
ob=B(45,65,5)

class A:
    a=1
    def a_disp(self):
        print('class A')
class B(A):
    b=2
    def b_disp(self):
        super().a_disp()
        print('class B')
class C(B):
    def c_disp(self):
        super().b_disp()
        print('class C')
class D:
    d=4
    def d_disp(self):
        print('class D')
class E(D):
    e=5
    def e_disp(self):
        super().d_disp()
        print('class E')
class F(C,E):
    f=6
    def f_disp(self):
        super().c_disp()
        super().e_disp()
        print('class F')
class G(F):
    g=7
    def g_disp(self):
        super().f_disp()
        print('class G')
class H(F):
    h=8
    def h_disp(self):
        super().f_disp()
        print('class H')
class I(F):
    def i_disp(self):
        super().f_disp()
        print('class I')

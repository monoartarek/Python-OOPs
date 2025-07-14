class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

class C(A):
    def method_C(self):
        print("Method C")

class D(B, C):
    def method_D(self):
        print("Method D")

obj = D()
obj.method_A()  # From A (via B and C)
obj.method_B()  # From B
obj.method_C()  # From C
obj.method_D()  # From D


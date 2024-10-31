class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b, B))
print(isinstance(b, A))


class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(B,Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')


apple = FruitFlavour()
print(FruitFlavour.__mro__)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# Check the MRO of class D
print(D.mro())
print(help(FruitFlavour))


class A:
    def c(self):
        return "Function inside A"


class B(A):
    def c(self):
        return "Function inside B"


class C(A, B):
    pass


class D(C):
    pass


d = D()
print(d.c())

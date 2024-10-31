from abc import ABC,abstractmethod

class A(ABC):
    def __init__(self,usn):
        super().__init__()
        self.usn=usn
        print("HI")
    
    @abstractmethod
    def hello(self):
        print("Hello ")

    def talk(self):
        print("Everyone talks")

class Stud(A):
    def __init__(self, usn,name):
        super().__init__(usn)
        self.name=name

    def hello(self):
         print("hello",self.name)
    
    def info(self):
        print(self.name,self.usn)



class C(A):
    def hello(self):
        return super().hello()

ob=Stud(20,"San")
ob.talk()
ob.hello()
ob.info()

ob1=C(22)
ob1.hello()
class Adult:
    def __new__(cls,name,age,*args,**kwargs):
        if age < 18:
            print("age must be above 18 and created a none object")
        else:
            return super().__new__(cls)
        
            
    def __init__(self, name, age):
        self.name=name
        self.age=age


ob=Adult("sandy",10)
          

print(ob)
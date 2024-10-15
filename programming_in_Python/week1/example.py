a=('dhk',7,9)
print(id(a))
b = ('dhk',7,9)
print(id(b))

a='y'
b=ord(a)
#print(b,file=open("ex.txt",'a'))

a=5
b=7
match a:
    case 7:
        print(a)
    case _:
        print("hi")

for i in range(5):
    j=1+i
        
print(j)       
print('dc'<'c')
print((5,7,9)>(2,8,77))
def div(a,b):
    try:    
       return a/b
    except Exception as e:
        return(e.__class__)
print(div(4,0))

with open("ex.txt", 'rb+') as f:
    
    print(f.readline())
    print(f.tell())
    print(f.fileno())
a = [4, 3, 47, 8]
a[2] = 10
a.extend(a)
print(a)


def ispal(str):
    st=0
    en=len(str)-1
    for x in str:
        if str[st]!=str[en]:
            return False
    return True

print(ispal("asda"))
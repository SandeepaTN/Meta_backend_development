a=[5,8,2,7,10,11]

def is_even(n):
    if n%2==0:
        return n
b=list(map(is_even,a))
print(b)
b=list(filter(is_even,a))
print(b)
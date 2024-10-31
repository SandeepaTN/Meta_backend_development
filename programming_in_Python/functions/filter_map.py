a=[5,8,2,7,10,11]

def is_even(n):
    if n%2==0:
        return n*4
b=list(map(is_even,a))
print(b)
b=list(filter(is_even,a))
print(b)


numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
   return numbers < 50


small = list(map(lesser, numbers))
print(small)


small = list(filter(lesser, numbers))
print(small)

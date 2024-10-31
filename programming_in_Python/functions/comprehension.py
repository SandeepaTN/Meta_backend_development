a=[1,10,5,4,7,8,12,15,17,16,18,6]
b=[x-1 for x in a if x%4==0]
c = [x - 1 if x % 4 == 0 else x for x in a]

d = [x - 1 if x % 5 == 0  else  -x if x%2==0  else x for x in a]
print(b)
print(c)
print(d)


a=[1,4,7]
b=[2,5,8,11]
ad={n:n*2 for n in range(10)}
print(ad)

bd={k:v for k,v in zip(a,b)}
print(bd)

sa={x for x in range(10,20) if x not in [12,14,16]}
print(sa)

a = [[96], [69]]

print(''.join(list(map(str, a))))


data = [2, 3,5,7,11,13,17,19,23,29,31,6,12]
gen_obj=(x for x in  data if x%2==0 and x%3==0 )
print(gen_obj)
for i in gen_obj:
    print(i)

def aaa():
    return
aaa()


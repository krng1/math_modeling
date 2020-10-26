def changer(a,b):
    a = 2
    b[0] = 'Good'
x = 10
L = [1, 2]
changer(x,L)
print(x)
print(L)  
def my_func(a = 1, b = 0):
    x= 3*a-b
    return x
print(my_func(b = 7))
 
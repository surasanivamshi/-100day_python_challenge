x = int(input("give a number"))
a = 2
while a<x/2:
    if (x%a==0):
        print("not prime number")
        break
    print('infinity')
    a=a+1
if a>=x/2:
    print('prime nbr')



from factor_multiple import fact   # import factor_multiple as vam
num1 = int(input("ente first number"))
num2 = int(input("enter second number"))
i= 2
k=2
my_list1=[]
my_list2= []
while num1>1:
    while num2>1:
       if num2%k==0:
            num2 = num2/k
            #print("factor", i)
            my_list2.append(k)
            #my_list2=list(set2)

       else:
          k = k + 1
    if num1%i==0:
        num1= num1/i
        my_list1.append(i)
        #my_list1=list(set1)

    else:
        i = i + 1

#print(my_list1)
#print(my_list2)
final=fact(my_list1,my_list2)
print(final)
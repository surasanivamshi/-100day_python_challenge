#x = int(input("give a number"))
#dupe=0
#temp1=x%10
#temp2=x/10
#c=temp1*100

#temp3=temp2%10
#temp4=temp2/10
#a=int(temp3)
#b=int(temp4)
#d=a*10
#answer = c+d+b
#print(answer)

x = int(input("give a number"))
rev = 0
data_temp = x
if (x<0):
    x = x*(-1)

while(x>0):
    temp1= x%10
    rev = rev*10+temp1
    x = (int(x/10))
#print(rev)
if( data_temp<0):
    print(-rev)
else:
    print(rev)




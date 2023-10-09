numbers = input('give the numbers with the spaces')
#now the given heights are to be fit in list
number_list=numbers.split() #here we are giving empty() because we seperated by space (we use , . )
#now in the list it is in string form so we need to convert into int
count=0
for k in number_list:
    count=count+1
for i in range(0,count):     #range is like we are taking index value
    number_list[i]=int(number_list[i])
    #print(height_list)
max_number=number_list[0]   #for ex [8,10,76,-12,4,5]
for number in number_list:
    if number>max_number:
        max_number=number
print(max_number)

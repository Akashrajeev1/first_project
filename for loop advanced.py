num=12345
sum=0
for i in range(len(str(num))):   #we cannot find lenght of num ,so convert it into str
    temp=num%10   #to get last value
    num=num//10   #to getrid of last value
    print(num)
    sum+=temp     #temp value will go into sum and add +1,
print(sum)

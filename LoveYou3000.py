a=3000
for number in range(1, a+1):
    c=0
    rpv=0
    temp=number
    for  i  in         range(1, temp+1):
        if temp%i==0:
            c+=1
    if c                                         ==2:
        while temp>0:
            rpv=rpv*10+(temp%10)
            temp=temp//10
        if rpv == number:
            print(number)
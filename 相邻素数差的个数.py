while True:
    n=int(input("please enter the test number:"))
    primelist=[1]*n
    difference=[0]*100
    a=1
    for i in range(0,n):
        if primelist[i]==1:
            b=abs(i+2-a)
            a=i+2
            c=int(b/2)
            difference[c]=difference[c]+1
            for j in range(2*i+2,n,i+2):
                primelist[j]=0
    del difference[0]
    print(difference)
    print("第i个数字表示相邻素数间隔为2i的对数")

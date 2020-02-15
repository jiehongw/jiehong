import math
import random
#输入循环次数和刷新概率
n=int(input("please enter the test number:" ))
p=float(input("please enter the possibility:"))
GetMeterial=0
GetNoMeterial=0
#进入大循环n次
for a in range(0,n):
    #初始化数据
    people1=3
    people2=3
    people3=3
    people4=3
    GameTime=250
    #前250秒的八次随机扣血
    for x in range(0,8):
        Num1=random.randrange(1,5)
        if Num1==1:
            people1=people1-1
        elif Num1==2:
            people2=people2-1
        elif Num1==3:
            people3=people3-1
        else:
            people4=people4-1
    if people1>0:
        #进入250到460秒的循环
        for y in range(0,211):
            #每秒进行的操作，判断是否材料刷新，是否随机扣血
            Num2=random.random()
            if Num2<p:
                #材料刷新，进入采集阶段，进行25秒采集阶段
                for z in range(0,26):
                    #依然是进行每秒的操作
                     GameTime=GameTime+1
                     if GameTime%30==0:
                         #随机扣血
                         Num1=random.randrange(1,5)
                         if Num1==1:
                             people1=people1-1
                         elif Num1==2:
                             people2=people2-1
                         elif Num1==3:
                             people3=people3-1
                         else:
                             people4=people4-1
                     #采集25秒后，判断是否存活
                if people1>0:
                    GetMeterial=GetMeterial+1
                    break
                else:
                    GetNoMeterial=GetNoMeterial+1
                    break
    else:
        GetNoMeterial=GetNoMeterial+1
Probabilityofsuccess=GetMeterial/n
print("the probability of success =",Probabilityofsuccess)
input("Press <enter>")  


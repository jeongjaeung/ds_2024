import random 
initial_money = 50
goal = 250
wins = 0

for i in range(100):
    cash = initial_money
    while cash>0 and cash<goal :
        num = random.randint(1,2)
        if num==1:
            cash += 1
        else: 
            cash -= 1
    if cash == goal : wins +=1
    if cash == 0 : continue
print('초기금액:$' ,initial_money)
print('목표금액:$' ,goal)
print('100번 중에서', wins, '번 성공')


p = 4
for i in range(1,6):
    print(""*p, sep="")
    print("*"*i)
    p -=1
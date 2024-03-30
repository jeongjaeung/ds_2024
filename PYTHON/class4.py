# #반복을 사용
# for i in range(1000):
#     print("방문을 환영합니다!")



# #리스트란? 
# slist = ["영어","수학","사회","과학"]
# print(slist) #영어, 수학, 사회, 과학을 출력
# #리스트의 인덱스
# slist[0] #영어를 출력
# #리스트 항목 변경
# slist[-1] = "컴퓨터" 
# print(slist) #영어, 수학, 사회, 컴퓨터를 출력



# #중간점검
# myList = [1,2,3,4,5]
# myList[0] = 0
# myList[-1] = 9
# print(myList)



#리스트에 동적으로 항목 추가
# list=[] #공백 리스트를 생성한다.
# list.append(1) #리스트에 정수 1을 추가한다.
# list.append(2) #리스트에 정수 2를 추가한다.
# list.append(6) #리스트에 정수 6을 추가한다.
# list.append(3) #리스트에 정수 3을 추가한다.
# print(list)



# n = int(input("정수를 입력하시오.:"))
# fact = n 
# for i in range(n, 0, 1):
#     fact = fact*i
# print(n, "!은", fact, "이다.")



# n각형 그리기
# import turtle as t
# t.shape("turtle") 
# s= t.textinput("", "몇 각형?:")
# n=int(s)
# for i in range(n):
#     t.forward(100)
#     t. left(360/n)
# t.mainloop()
# t.bye()



# # 방정식의 해 구하기 XXXXX
# COUNT =10000
# START = 1.0
# END = 2.0
# for i in range(COUNT):
#     x = START + i*((END-START)/COUNT)
#     print(x)
#     f = (x**2 -x -1)
#     if abs (f-0.0) < 0.01 : #허용오차를 정해줌 #0.0을 빼는 이유 : 
#         print("방정식의 해는", x)

# # 조건 제어 반복(while)
# Target = 2000
# money = 1000
# year = 0 

# 구구단 출력 XXXXX
# dan = int(input("원하는 단은?"))
# i =1 
# while i<10 :
#     print("%s*%s=%s" %(dan,i, dan*i))
#     i = i +1
    


# 숫자 맞추기 게임 #시도횠수 추가
# import random
# print("1부터 100사이의 숫자를맞추시오")
# answer = random.randint(1,100)
# guess = 0

# while guess != answer:
#     guess = int(input("숫자를 입력하시오:"))
#     if guess>answer:
#         print("높음!")
#     elif guess<answer:
#         print("낮음!")
#     else:
#         print("정답입니다.!")



# for y in range(5,0,-1) :
#     for x in range(y) :
#         print("*", end="")
#     print("")

# for y in range(1,6) :
#     for x in range(6-y) :
#         print("*", end="")
#     print("")

# for y in range(1,6) :
#     for x in range(6-y) :
#         print("*", end="")
#     print("")

# for y in range(1,6) :
#     for x in range(y):
#         print("",end="")
#         print("*", end="")
#     print("")

# for i in range(5,0,-1) :
#     print(" "*(5-i), "*"*i, end="")
#     print("")

# persons = ["Kim", "Park", "Lee"]
# restaurants = ["Korean", "American", "French", "Chinese"]
# for person in persons:
#     for res
    
# bunja = 4.0
# bunmo = 1
# pi=0
# loop = int(input("반복횟수:"))

# for loop in range(1, loop):
#     pi = pi + bunja/bunmo
#     bunja *= -1
#     bunmo += 2
# print(pi)
    
# import turtle as t 
# import random
# for i in range(100):
#     length = random.randint(1, 100)
#     t. forward(length)
#     angle = random.randint(-180, 180)
#     t. right(angle)
# t.mainloop()
# t.bye()


import turtle as t 
t. shape("turtle")
for i in range(100):
    t. forward(10+i/5)
    t. right(30-i/1000)
t.mainloop()
t.bye()

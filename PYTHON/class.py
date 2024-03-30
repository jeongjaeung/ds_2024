# #배송비 계산 프로그램 #00000
# price = int(input("상품의 가격:"))
# if price > 20000 :
#     shipping_cost = 0
# else :
#     shipping_cost = 3000
# print("배송비=", shipping_cost)



# 실수비교 #xxxxx
# from math import sqrt
# n =  sqrt(3)
# if n*n == 3 :
#     print("sqrt(3)*sqrt(3)은 3과 같다.")
# else :
#     print("sqrt(3)*sqrt(3)은 3과 같지 않다.")



# #산술퀴즈프로그램 #00000
# import random
# x = random.randint(1,100)
# y = random.randint(1,100)
# answer = int(input(f"{x}+{y}="))
# 정답확인 = (answer == (x+y))
# print(정답확인)



# # 짝홀 판단 by 조건연산자 #00000
# number = int(input('정수를 입력하시오:'))
# print('짝수입니다.' if number % 2 == 0 else '홀수입니다.')



# #세일 가격 계산 #00000
# price = int(input('정가를 입력하시오 (만원):'))
# print('10층에서 사은품을 받아가세요.' if price>=100 else "")
# print(f"할인된 가격= {int(price*0.85) if price>=100 else int(price*0.9)}")
# print(price*0.9 if price<100 else price*0.85)



#피이썬카드와 가격 배송료 유무 by논리연산자 #00000
# price = int(input('가격을 입력하시오.:'))
# card = input('카드 종류를 입력하시오.:')
# if price > 20000 and card == "python" :
#     print('배송료가 없습니다.')
# else :
#     print('배송료는 3000원입니다.')



#드모르간의 법칙 #00000
# country = input("배송국을 입력하시오:")
# province = input("배송지역을 입력하시오:")
# if country !="한국" or province !="제주":
#     print('배송비는 8000원 입니다.')
# else:
#     print("배송비는 무료입니다.")



# #물의 상태 출력하기 #00000
# temp = int(input('온도를 입력하시오:'))
# if temp>=100:
#     print('기체입니다.')
# elif temp <=0:
#     print('고체입니다.')
# else :
#     print('액체입니다')    

#version2
# temp = int(input('물의 온도를 입력하시오.:'))
# if temp>= 100:
#     print('기체입니다.')
# elif temp>= 0:
#     print('액체입니다.')
# else:
#     print('고체입니다.')



# #동전 던지기 게임 #다시해보기
# import random
# print('동전 던지기 게임을 시작합니다.')
# coin = random.randint(0,1)
# if coin == 0:
#     print('앞면입니다.')
# else:
#     print('뒷면입니다.')
# print('게임을 종료합니다.')



# #거북이 제어하기
# import turtle as t
# t.clearscreen()
# t.setup(500,500)
# command = input('명령을 입력하시오.:')
# if command == l :



# #거북이 제어하기 #들여쓰기의 중요성
# import turtle as t
# t.shape('turtle') # 이 문장 없으면 화면 안뜸
# while True: #실행버튼 계속 누를 필요없이 r이랑 l누르면 돼
#     command = input('명령을 입력하시오:')
#     if command == 'l':
#         t. left(90)
#         t. forward(30)
#     elif command == "r":
#         t. right(90)
#         t. forward(30)
#     elif command =="q":
#         print("게임을 종료합니다.")
#     else:
#         print("잘못된 명령입니다.")



# 거북이로 사각형 그리기 #다시해보기
# import turtle as t
# size = int(input("사각형의 크기를 입력하시오.:"))
# t. forward(size)
# t. right(90)
# t. forward(size)
# t. right(90)
# t. forward(size)
# t. right(90)
# t. forward(size)
# turtle.mainloop()
# turtle.bye()



# #BMI 계산하기
# weight = int(input('몸무게(kg):')) #int보단 float을 쓰는게 맞음
# height = int(input('키(cm):')) #int보단 float을 쓰는게 맞음
# # print("당신의 몸무게는: "+int(weight/(height*height))) #여기서 틀렸음
# bmi = (weight/(height**2)) #나누기 하면 실수인데 앞에 int로 묶으면 에러가 나니까 결과값이 0이 나옴
# print("당신의 BMI는 ", bmi)



# #구의 부피 구하기
# radius = float(input("반지름을 입력하시오.:"))
# volume = 4/3*3.141592*(radius**2) #pi라고 쓰면 안돼. 정의되어 있지 않음.
# #print('volume') #틀린문장
# print(volume) #옳은문장



#자동판매기 프로그램 #꼭 다시해보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# price = int(input("물건값을 입력하시오(원):"))
# money1000 = int(input("천원개수:"))
# money500 = int(input("오백원개수:"))
# money100 = int(input("백원개수:"))
# total = money1000*1000 + money500*500 + money100*100
# change = total - price
# number500 = change//500
# change= change%500
# number100 = change//100
# change = change%100
# number10 = change//10 
# print(number500*500 + number100*100 + number10*10)



# #배송비 계산 프로그램 #다시해보기!!!!!!!!!!!!!!!!!!!!!!!!!!
# country = input('배송지를 입력하세요:')
# price = int(input("상품의 가격을 입력하세요:"))
# if country == "korea":
#     if price >= 20000:
#         print("배송비는 없습니다.")
#     else :
#         print("배송비는 3000원입니다.")
# if country == "usa":
#     if price >= 100000:
#         print('배송비는 없습니다.')
#     else:
#         print("배송비는 8000원입니다.")
        


# #연속 if문 (학점입력) 00000
# score = int(input('점수를 입력하시오 :'))
# if score>=90:
#     print("성적은 A입니다.")
# elif score>=80:
#     print("성적은 B입니다.")
# elif score>=70:
#     print("성적은 C입니다.")
# else:
#     print("성적은 D입니다.")



# #리히터 규모
# scale = float(input('리히터 규모를 입력하시오.:'))
# if scale<2 :
#     print("지진계에 의해서만 탐지 가능합니다.")
# elif scale<4 :
#     print("물건들이 흔들리거나 떨어집니다.")
# elif scale<7 :
#     print("빈약한 건물에 큰 피해가 있습니다.")
# elif scale<8 :
#     print("지표면에 균열이 발생합니다.")
# # else scale<=9 : #틀린문장 else 뒤는 바로 :을 써야함
# else :
#     print("대부분의 구조물이 파괴됩니다.")



# #사용자 입력 검증하기. #다시 해보기
# choice = int(input("메뉴를 선택하세요:"))
# print
# if choice>=1 and choice<=3:
#     print()



#축구 수비 게임
# import random 
# computer = random.randint(1,3)
# user = input("어디를 수비하시겠어요?(왼쪽:1, 중앙:2, 오른쪽:3):")
# if computer == user:
#     print('수비성공')
# else:
#     print('수비실패')

# import random
# 수비 = input('어디를 수비하시겠어요?(왼:1, 중:2, 오:3):')
# if random.randint(1,3) == 수비:
#     print("수비성공")
# else:
#     print("수비실패")

# # 알람시간 출력
# time = map(int, input("알람시간을 입력하시오.:").split())
# print(alarm, alarm[0], alarm[1])
    
#도형 그리기(by터틀그래픽)
input("도형을 선택하시오:")
import turtle as t

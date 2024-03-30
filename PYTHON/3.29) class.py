def get_area(radius):
    area = 3.14*radius**2
    return area

result = get_area(3)
print("반지름이 3인 원의 면적=", result)

#중간점검 3번 문제
def f(x,y):
    return(x,y)

# #피자 크기 비교
# PI : 3.14
# def pizza_area(radius): #함수정의
#     area = PI*(radius**2)
#     return(area)
# area1 = pizza_area(20) #호출
# area2 = pizza_area(30)
# print(area1*2)
# print(area2)

#주급계산프로그램
def weeklyPay(wage,hour):
    if wage>30:
        weeklyPay = 30*wage + ((hour-30)*(wage*1.5))
    else:
        weeklypay = hour*wage
    return weeklyPay
wage = int(input('시급을 입력하시오:'))
hour = int(input('근무시간을 입력하시오:'))
print('주급은', weeklyPay(wage,hour))

#사각형을 그리는 함수 작성하기
import turtle as t
t.shape("turtle")

def square(length):


#팩토리얼 계산 프로그램
def factorial(n):
    if n==1:
        return(1)
    else:
        return n*factorial(n-1)
n=eval(input("정수를 입력하시오:"))
print(n, "!=", factorial(n))


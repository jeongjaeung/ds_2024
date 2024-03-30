money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")


money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")



money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")



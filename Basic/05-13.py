balance, money, select = 0, 0, 0

money=int(input("돈을 넣어주세요"))
select = int(input("음료를 골라주세요 1. 포도주스 \n 2. 오렌지주스"))
balance = money
if select ==1:
    if money >= 100:
        print("포도주스")
        money = balance-100
    else:
        print("금액부족")
elif select == 2:
    if money >= 200 :
        print("오렌지주스")
    else:
        print("금액부족")
else:
    print("잔고부족")
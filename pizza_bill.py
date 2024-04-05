print("파이썬 피자에 오신 것을 환영합니다!")
pizza_size = input("원하시는 피자사이즈를 눌러 주세요! (S, M,L)")
bill  = 0

if pizza_size == "S" or pizza_size == "s":
    bill = 15000
    print(f"스몰은 {bill}원 입니다.")
elif pizza_size == "M" or pizza_size == "m":
    bill = 20000
    print(f"미디움은 {bill}원 입니다.")
elif pizza_size == "L" or pizza_size == "l":
    bill = 30000
    print(f"라지는 {bill}원 입니다.")
else:
    print("잘못 입력하셨습니다. 다시 실행해 주세요!")
    
wants_peperoni = input("페페로니를 추가는 2천원입니다. 추가하시겠습니까? 추가(Y) 아니오(N)")
if wants_peperoni == "Y" or wants_peperoni == "y":
    bill += 2000
    print(f"페페로니를 추가한 금액은 {bill}원 입니다.")
    
wants_cheese = input("치즈 추가는 3천원입니다. 추가하시겠습니까? 추가(Y) 아니오(N)")
if wants_cheese == "Y" or wants_cheese == "y":
    bill += 3000
    print(f"치즈를 추가한 금액은 {bill}원 입니다.")
    
print(f"총 지불하실 금액은 {bill}원 입니다.")

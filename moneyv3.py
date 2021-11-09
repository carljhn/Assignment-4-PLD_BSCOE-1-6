import math

def getMax_aplsChange():
    money_=int(input("You have an amount of: "))
    apls_cost=int(input("An apple costs: "))
    max_apls=int(money_/apls_cost)
    total_=max_apls*apls_cost
    change_=money_-total_
    return max_apls, change_
import math

def getTotalCost():
    apples_quant=int(input("How many apples do you want?: "))
    oranges_quant=int(input("How many oranges do you want?: "))
    apls_cost=apples_quant*20
    orngs_cost=oranges_quant*25
    total_cost=apls_cost+orngs_cost
    return total_cost
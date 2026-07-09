from typing import Union

def  calculate_tax(price:Union[int, float])->float:
    return price * 0.13

print(calculate_tax(100))
print(calculate_tax(88.99))
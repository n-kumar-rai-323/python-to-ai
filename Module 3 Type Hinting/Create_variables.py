def say_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Hello {name}"


def square(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    return number * number


def discount(price: float) -> float:
    if not isinstance(price, float):
        raise TypeError("Price must be a float")
    return price * 0.9


def get_name():
    try:
        user_input = input("Enter your name: ")
        print(say_name(user_input))
    except TypeError as e:
        print(f"Error: {e}")


def get_square():
    try:
        user_input = int(input("Enter a number: "))
        print(f"Square: {square(user_input)}")
    except ValueError:
        print("Please enter a valid integer.")
    except TypeError as e:
        print(f"Error: {e}")


def get_discount():
    try:
        user_input = float(input("Enter a price: "))
        print(f"Discount Price: {discount(user_input):.2f}")
    except ValueError:
        print("Please enter a valid price.")
    except TypeError as e:
        print(f"Error: {e}")


def get_admin_status():
    try:
        user_input = input("Are you admin? (true/false): ").strip().lower()

        if user_input == "true":
            is_admin = True
        elif user_input == "false":
            is_admin = False
        else:
            raise ValueError("Please enter only 'true' or 'false'.")

        print(f"Admin Status: {is_admin}")

    except ValueError as e:
        print(f"Error: {e}")

names: list[str] =[
    "Ram",
    "Hari",
    "Sita",
    "Gita"
]

print(names)
marks:list[int]=[
    90,
    50,
    70
]
print(marks)


student:dict[str,str]={
    "name":"Nishan",
    "city":"Kathmandu"
}
marks:dict[str,int]={
    "Math":95,
    "Science":88
}

from typing import Optional

def get_user(phone: Optional[str])->str:
    if phone:
        return phone
    return "No Phone"
from typing import Union
price:Union[int, floa]=100

def calculate(value: Union[int, float])->float:
    return value * 2
from typing import Any
data: Any ="Hello"

from typing import Literal
Role = Literal[
    "admin",
    "user",
    "guest"
]

from typing import TypedDict
class Student(TypedDict):
    name:str
    age:int

student:Student={
    "name":"Nishan",
    "age":25
}

class Weather(TypedDict):
    city:str
    temperature:float
    condition:str

def get_weather(city:str)->Weather:
    return{
        "city":city,
        "temperature":29.5
        "condition":"Sunny"
    }
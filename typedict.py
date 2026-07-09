from typing import TypedDict

class Student(TypedDict):
    name:str
    age:int
    email:str
    
student: Student={
    "name":"Nishan",
    "age":25,
    "email":"nishan@gmail.com"
}
print(student)
from typing import TypedDict

class Weather(TypedDict):
    city: str
    temperature: float
    condition: str


def get_weather(city: str) -> Weather:
    return {
        "city": city,
        "temperature": 29.5,
        "condition": "Sunny"
    }

weather = get_weather("Kathmandu")

print(weather)
from typing import Literal

Role = Literal[
    "admin",
    "user",
    "guest"
]

def login(role: Role):
    print(f"Welcome {role}")
    
login("admin")
login("user")
login("manager")
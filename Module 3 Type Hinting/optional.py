from typing import Optional

def get_phone(phone: Optional[str])->str:
    if phone is None:
        return "Phone not provided"
    return phone

print(get_phone("8987987987"))
print(get_phone(None))
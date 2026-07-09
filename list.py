# An e-commerce website stores product names.
products:list[str]=[
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor"
]

for product in products:
    print(product)
    

# A schoole stores student's exam scores
marks:list[int]=[
    80,
    75,
    95,
    89
]

average = sum(marks)/len(marks)
print(f"Average Marks: {average}")
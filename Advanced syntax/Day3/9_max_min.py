"""
min(可迭代对象，key=函数)

"""

people = [
    {"name": "Chr", "age": 22},
    {"name": "Ch", "age": 25},
    {"name": "C", "age": 29},
    {"name": "Chris", "age": 2},
]

print(max(people, key=lambda people: people["age"]))
print(min(people, key=lambda people: people["age"]))







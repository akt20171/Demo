def get_greeting(user):
    name = user["name"]
    age = user["age"]
    return f"Hello {name}, you are {age} years old!"

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 28},
    {"name": "Carol", "age": 25}
]

for user in users:
    print(get_greeting(user))
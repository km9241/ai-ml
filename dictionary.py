person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer"
}
print(person["name"])   # Output: Alice
print(person.get("age"))  # Output: 25
#Use get() to avoid errors if the key is missing.
person["age"] = 26           # Update
person["city"] = "Mumbai"    # Add new key-value pair
person = {"name": "Alice", "age": 25}

print(person.keys())      # dict_keys(['name', 'age'])
print(person.values())    # dict_values(['Alice', 25])
print(person.items())     # dict_items([('name', 'Alice'), ('age', 25)])
for key in person:
    print(key, person[key])
"""or key in person iterates over the dictionary’s keys ("name", "age", "city").

person[key] accesses the value for each key.

"""

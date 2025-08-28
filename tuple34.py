person = ("Alice", 25, "Engineer")#its immutable
print(person)  # Output: ('Alice', 25, 'Engineer')
print(person[0])  # 'Alice'
print(person[1])  # 25
print(len(person))  # Output: 3
t = (1, 2, 2, 3, 2)
print(t.count(2))  # Output: 3
t = (1, 2, 2, 3, 2)
print(t.count(2))  # Output: 3
for item in person:
    print(item)
students = (("John", 18), ("Jane", 19), ("Jim", 17))
for name, age in students:
    print(name, age)
person[0] = "Bob"  # ❌ This will cause an error


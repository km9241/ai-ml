def square(x):
    return x * x

def add_five(y):
    return y + 5

# Calling one function inside another
result = add_five(square(3))

print(result)  # Output: 14

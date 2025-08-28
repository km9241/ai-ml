for x in range(10):#
    print(x)
for i in range(1, 6):
    print(i)
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']

for fruit in fruits:
    if fruit == 'cherry':
        continue  # Skip 'cherry' and go to next item
    if fruit == 'grape':
        break     # Stop the loop when 'grape' is found
    print(fruit)
x = 1
while x <= 5: #A while loop keeps running as long as a condition is True.
    print(x)
    x += 1  # increase x by 1 in every loop
    

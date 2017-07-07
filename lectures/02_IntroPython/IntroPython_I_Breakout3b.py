# A simple for loop to find sum of all odd numbers up to 100
total = 0
for i in range(100):
    if i % 2 == 1:
        total += i
print(total)

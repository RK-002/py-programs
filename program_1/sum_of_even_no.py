# Calculate the sum of even numbers from 0 to 10
sum = 0
for n in range(0, 11):
    if (n % 2 == 0):
        sum = sum + n
print(sum)
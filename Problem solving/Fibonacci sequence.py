# # fibonacchi serise
# n = int(input("Enter number: "))
a = 0
b = 1
sum = 0

for i in range(5):
    print(a, end=" ")
    sum = a + b
    a = b
    b = sum

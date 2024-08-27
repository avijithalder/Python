# Prime Numbers

n = int(input("Enter Number: "))

for i in range(2, n):
    if n % 2 == 0:
        print(f"{n} Not Prime ")
        break
else:
    print(f"{n} Prime number")


numbers = int(input("Enter the number: "))

if number == 0:
    count = 1
else:
    count = 0
    while number > 0:
    number //= 10
    count += 1
print(f"The number of digit is: (count)")

number = int(input("Enter the number: "))
digit_sum = 0

while number > 0:
    last_digit = number % 10
    digit_sum += last_digit
    number //= 10
print(f"The sum of the digit is: {digit_sum}")

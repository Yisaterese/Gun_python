user_input = int(input("Enter number from 1 and above: "))
sumOf_even_numbers = 0
sumOf_odd_numbers = 0
for numbers in range(1, user_input+1):
    if user_input < 1: print("Enter a valid number from 1 and above")
    if numbers % 2 == 0: sumOf_even_numbers += numbers
    if numbers % 2 == 1: sumOf_odd_numbers += numbers
print(f"the sum of even numbers are: {sumOf_even_numbers}")
print(f"the sum of odd numbers are: {sumOf_odd_numbers}")


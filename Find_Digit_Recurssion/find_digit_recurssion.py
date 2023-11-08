def findDigit(lst):
    #Base Case
    if (1<lst<10):
        return 1
    else:
        return 1 + findDigit(lst // 10)
        
print(findDigit(200))
# def count_digits(n):
#     # Base case: If the number is 0, it has 1 digit
#     if n == 0:
#         return 1
#     # Recursive case: Remove the last digit and count the rest
#     else:
#         return 1 + count_digits(n // 10)

# # Input integer
# num = int(input("Enter an integer: "))

# # Call the recursive function to count digits
# result = count_digits(abs(num))

# print(f"The number of digits in {num} is {result}")
#Example-1: Check if a number is prime
# Number = int(input('Enter the number: '))
# is_prime = True
# for i in range(2,Number):
#     if  Number % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(Number, ' is a prime number')
# else:
#     print(Number, ' is not a prime number')


#Example-2:  Find factorial of a number
# Number = int(input('Enter the number: '))
# Factorial = 1
# i = 1
# while i <= Number:
#     Factorial = Factorial * i
#     i += 1

# print(Factorial)


#Example-3: Fibonacci sequence up to N terms
# n = int(input('How many terms? '))
# a, b = 0, 1
# i = 0
# while i < n:
#     print(a)
#     a,b = b, a+b
#     i += 1


#Example-4: Reverse a number
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print("Reversed number:", rev)


#Example : Reverse a Word
# Word = input('Enter the word: ')
# for char in range(len(Word) - 1, -1, -1):
#     print(Word[char], end="")

# print('\n')


#Example-6: Construct Pattern (Diamond Pattern)
# Step = int(input('Enter the number of line you want: '))
# for i in range(Step):
#     for j in range (i):
#         print('* ', end = '')
#     print('')


# for i in range(Step, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
#Basic Level
#Example 3: Print Numbers from 1 to 10
for i in range(1,11):
    print (i)

#Example 2: Python program to print all the even numbers within the given range.
Range = int(input('ENter the range of your concern: '))
for i in range(1, Range+1):
    if i%2 ==0:
        print (i)


#Example 3: Python program to calculate the sum of all numbers in a given range.
Start = int(input('Enter thr number you want to start with: '))
Limit = int(input('Enter the number you want to stop: '))
sum = 0
for i in range(Start, Limit+1):
    sum = sum + i
    i = i+1

print (sum)

#Example 4: Python program to calculate the sum of all the odd numbers within the given range.
Start = int(input('Enter thr number you want to start with: '))
Limit = int(input('Enter the number you want to stop: '))
sum = 0
for i in range(Start, Limit+1):
    if i % 2 != 0:
        sum = sum +i

print(sum)


# Example 5: Python program to print a multiplication table of a given number
Number = int(input('Enter the of multiplication table: '))
for i in range(1,11):
   print (Number," x",i," =",Number*i)


# Example 6: Python program to check if the given string is a palindrome.
Word = input('Enter a word: ')
reverse_string = ""
for i in Word:
    reverse_string = i + reverse_string

if Word == reverse_string:
    print(Word,' is a palindrome')
else:
    print(Word,' is not a palindrome')



        

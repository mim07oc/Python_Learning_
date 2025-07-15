#Ex-1: Check if a Number is Odd or Even
number =int(input('Enter a Number: '))
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')


#Find the Greatest
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("You entered:", numbers)
greatest = max(numbers)
print('The greatest num is: ', greatest)

# CGPA Grading System
Number_of_Course = int(input('Enter the total number of courses'))
List_of_marks = []
total_CGPA = 0
for i in range(Number_of_Course):
    marks = int(input(f'Enter marks for course {i+1}: '))
    List_of_marks.append(marks)
    if marks >= 80:
        CGPA = 4
    elif marks >= 75:
        CGPA = 3.75
    elif marks >= 70:
        CGPA = 3.50
    elif marks >= 65:
        CGPA = 3.25
    elif marks >= 60:
        CGPA = 3
    elif marks >= 55:
        CGPA = 2.75
    elif marks >= 50:
        CGPA = 2.50
    elif marks >= 45:
        CGPA = 2.25
    elif  marks >= 40:
        CGPA = 2
    else:
        CGPA = 0
    total_CGPA += CGPA

Average_CGPA = total_CGPA / Number_of_Course
print(f"Your average CGPA is: {Average_CGPA:.2f}")

#Leap Year Checker
Year = int(input('Enter the year'))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, 'is a leap year')
else:
    print(Year, 'is not a leap year')


# Vowel or Consonant Checker (Word Version)
Words = input('Enter the word: ')
vowel = 'aeiou'
vowel_count = 0
cons_count = 0
for char in Words:
    if char.isalpha():
        if char.lower() in vowel:
            vowel_count +=1
            print (char, 'is a vowel')
            print(vowel_count)
        else:
            cons_count +=1
            print(char,'is a consonent')
            print(cons_count)
    else:
        print(char,'is not a letter')





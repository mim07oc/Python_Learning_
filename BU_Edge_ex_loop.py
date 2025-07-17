"""Example-1:  Firstly take N and than N strings as input. Strings can be both 
uppercase and lowercase. Concat them and print a single string 
in Camelcase."""
N = int(input('Type the number of strings: '))
List = []
for i in range(N):
    s = input()
    List.append(s)
ans =""
for s in List:
    ans+=s[:1].upper()
    ans+=s[1:].lower()

ans =ans[:1].lower() +ans[1:] 
print(ans)


'''Example-2:  Write a Python program that computes the greatest common 
divisor (GCD) of two positive integers.'''
a = int(input('Enter the first num: '))
b = int(input('Enter the second num: '))
n = min (a, b)
GCD = 0
for i in range(1, n+1):
    if a % i == 0 and b % i == 0:
        GCD = i

print(f"The GCD of {a} and {b} is {GCD}.")


'''Example-3:  Write a Python program to find the least common multiple (LCM) 
of two positive integers.'''
a = int(input('Enter the first num: '))
b = int(input('Enter the second num: '))
for i in range(max(a, b), 1 + (a * b), max(a, b)):
    if i % a == i % b == 0:
        lcm = i
        break

print("LCM of", a, "and", b, "is", lcm)

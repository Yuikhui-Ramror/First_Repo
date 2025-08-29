#Checks if anything is a palindrome or not

#Simple version: String Slicing

char = input("Enter char: ")
if char[::-1] == char:
    print("Char is a palindrome")
else:
    print("Not a palindrome")

#Simple version 2: Using a loop

is_palindrome = True

for i in range(len(char) // 2):
    if char[i] != char[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Char is a palindrome")
else:
    print("Not a palindrome")
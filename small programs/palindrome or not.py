def check_palindrome(str1):
    if str1[::-1]==str1:
        return True
    else:
        return False

string = input("Enter the word or sentence to check palindrome:")
result = check_palindrome(string)
if result:
    print(f"The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")

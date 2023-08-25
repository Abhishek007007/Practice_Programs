def palindrome(str1):
    revstr1 = str1[::-1]
    if(str1 == revstr1):
        print(str1," is a palindrome")
    else:
        print(str1," is not a palindrome")


str1 = input("Enter the string :")
palindrome(str1)
def palindrome_checker_2019_2_60_057(str):
    if str == str[::-1]:
        return 'Palindrome'
    else:
        return 'Not palindrome'

string = input("Enter string: ")
print(palindrome_checker_2019_2_60_057(string))


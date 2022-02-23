string = input("Enter a string: ")
n = int(input("Enter integer: "))
if(n<len(string)):
    print(string[n+1:])
else:
    print("length of string is lower than n!")


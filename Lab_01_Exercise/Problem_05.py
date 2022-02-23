def prime_find_2019_2_60_057(num):
    if num>1:
        for i in range(2, num):
            if(num%i==0):
                return 'Not a Prime Number'
        else:
            return 'prime number'

n= int(input("Enter a number: "))
print(prime_find_2019_2_60_057(n))


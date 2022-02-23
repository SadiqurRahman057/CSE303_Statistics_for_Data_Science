N = int(input("Enter the value of N: "))
series= 0
for i in range(1,N+1,1):
    series = series+(i*i)
print("The value of the series is: ",series)
n= int(input("Enter a number:"))
F1= 0
F2= 1
for i in range(2,n):
    F= F1 + F2
    F1= F2
    F2= F
print("Fibonacchi number: ",F2)


list=[1,2,3,4,5]
total = 0
for i in range(0, len(list)):
    if(i%2)==0:
        total= total+list[i]
print("Sum of the even index: ",total)
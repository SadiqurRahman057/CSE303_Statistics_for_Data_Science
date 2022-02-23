def largest_number_2019_2_60_057(list):
    max=-999999
    for i in range(0, len(list)):
        if(list[i]>max):
            max = list[i]
    return max
def smallest_number_2019_2_60_057(list):
    min=9999999
    for i in range(0, len(list)):
        if(list[i]<min):
            min =list[i]
    return min
list=[1,2,3,4,5,6,7,8,9]
print("Largest number :",largest_number_2019_2_60_057(list))
print("Smallest number: ",smallest_number_2019_2_60_057(list))
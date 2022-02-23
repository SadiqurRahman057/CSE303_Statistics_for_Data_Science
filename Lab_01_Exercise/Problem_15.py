list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
newlist=[]
for i in range(0,len(list1)):
    x=list1[i]
    if(x%2!=0):
        newlist.append(x)
for i in range(0,len(list2)):
    y=list2[i]
    if(y%2==0):
        newlist.append(y)
print(newlist)

# # Indexing 
# x = [3, "hello", 1.2] 
# print ("x[0]: ", x[0]) 
# print ("x[1]: ", x[1]) 
# print ("x[-1]: ", x[-1]) 
# # the last item print ("x[-2]: ", x[-2]) # the second to last item

# # Indexing beyond length 
# x = [3, "hello", 1.2] 
# print (x[:100])
# print (len(x[:100]))

# Slicing print 
x = [3, "hello", 1.2]
("x[:]: ", x[:]) # all indices 
print ("x[1:]: ", x[1:]) # index 1 to the end of the list 
print ("x[1:2]: ", x[1:2]) # index 1 to index 2 (not including index 2) 
print ("x[:-1]: ", x[:-1]) # index 0 to last index (not including last index)
# # Creating a list
# x= [3,"hello",1.2]
# print(x)

# # creating a tuple
# x=(3.0,"hello")
# # tuples start and with ()
# print(x)

# # sets
# text = "SDS IN Python"
# print(set(text))
# print(set(text.split(" ")))

# # list comprehension
# # Grab every letter in string
# lst = [x for x in 'word']
# print(lst)
# # Check for even numbers in a range
# lst = [x for x in range(11) if x % 2 == 0]
# print(lst)
# # Convert Celsius to Fahrenheit
# celsius = [0,10,20.1,34.5]
# fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]
# print(fahrenheit)
# #nested list comprehension
# lst = [ x**2 for x in [x**2 for x in range(11)]]
# print(lst)

#Dictionaries
phonebook = { "John" : 938477566, "Jack" : 938377264, "Jill" : 947662781 }
print(phonebook)
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

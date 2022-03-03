def filterVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E' , 'I', 'O', 'U']
    if string not in vowels:
        return True
    else:
        return False
print("After Removing all of the vowels the string is:",end= " ")
string = "Practice Problems to Drill List Comprehension in Your Head."
filteredVowels = filter(filterVowels, string)
for vowel in filteredVowels:
    print(vowel, end="")

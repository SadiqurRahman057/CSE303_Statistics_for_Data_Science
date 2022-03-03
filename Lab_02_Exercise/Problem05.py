string = "Practice Problems to Drill List Comprehension in Your Head"
letters = string.split()
print(f"All of the words in a string that are less than 5 letters are: {[letter for letter in letters if len(letter) < 5]}")



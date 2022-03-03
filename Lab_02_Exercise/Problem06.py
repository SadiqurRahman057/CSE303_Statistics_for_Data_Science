from itertools import count


string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
count_char= {char : len(char) for char in words for words in string}

for i, j in count_char.items():
    print(f" {i}:{j} words")


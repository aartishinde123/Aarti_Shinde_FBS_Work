# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. 
# Use Python set data type.

strings = [
    "python is easy",
    "python is powerful",
    "easy learning python"
]

# step 1: split all strings into words
words = []
for line in strings:
    words.extend(line.split())

# step 2: get unique words using set
unique_words = set(words)

# step 3: count frequency
freq = {}
for word in unique_words:
    freq[word] = words.count(word)

# output
print("Unique words:", unique_words)
print("Word Frequency:", freq)

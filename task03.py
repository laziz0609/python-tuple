words = ("apple", "banana", "strawberry", "kiwi")

long_word = words[0]

for word in words:
    if len(word) > len(long_word):
        long_word = word
        
print(long_word)
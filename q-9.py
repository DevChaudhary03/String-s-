a = "Everyone loves data science"
words = a.split()

reversed_words = []
for i in words:
    reversed_words.append(i[::-1])

result = ' '.join(reversed_words)

print(result)

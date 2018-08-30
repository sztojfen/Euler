f = open("p042_words.txt", "r")
words = f.read()

words = words.replace('"',"")
words = words.split(",")

triangle_numbers = [n*(n+1)/2 for n in range(1, 1000)]

def word_sum(word):
    return sum([ord(c) - 64 for c in word])

result = 0
for word in words:
    if word_sum(word) in triangle_numbers:
        result += 1

print result
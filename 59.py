import itertools
from pprint import pprint

f = open('p059_cipher.txt')
l = f.readline().split(",")

key_range = range(ord('a'), ord('z') + 1)

key_list = ([x for x in itertools.permutations(key_range, 3)])

solutions = {}

for key in key_list:
    decrypted = []
    for i in range(len(l)):
        decrypted.append(chr(int(l[i]) ^ key[i % 3]))
    decrypted = ''.join(decrypted)
    print decrypted
    if "the" in decrypted and "to" in decrypted and "and" in decrypted and "of" in decrypted and "be" in decrypted:
        secret = chr(key[0]) + chr(key[1]) + chr(key[2])
        solutions[secret] = decrypted

pprint(solutions)
sum =+ 0
for letter in solutions["god"]:
    sum += ord(letter)

print sum

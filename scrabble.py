f = open("slowa.txt", "r")
##### slowo po slowie ######
# word = True
# while word:
#     word = f.readline().replace('\n', '',).replace('\r', '').replace(' ', '')
#     if 'v' in word:
#         print word


##### STATYSTYKA ############
words = f.read()
words = words.replace('\n', '',).replace('\r', '').replace(' ', '').decode('UTF-8')

counter = {}

for letter in words:
    if letter == "\n":
        continue
    if letter not in counter.keys():
        counter[letter] = 1
    else:
        counter[letter] += 1

total = len(words)
for key in counter.keys():
    print "literka: " + key + '--> ' + str(round(float(counter[key])/total*100, 2)) + "%"

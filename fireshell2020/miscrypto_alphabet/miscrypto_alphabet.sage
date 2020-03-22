def let2num(a):
	return ord(a) - 97

alphabet = [[0 for j in range (0,26)] for i in range (0,26)]

words = ["apple", "bear", "cat", "dog", "egg", "fish", "goat", "hat", "igloo", "jacket", "kite", "lion", "monkey", "nose", "ostrich", "pig", "queen", "rabbit", "sun", "turtle", "umbrella", "van", "wagon", "xray", "yoyo", "zebra"]

for i in range (0,26):
	for j in range (0,len(words[i])):
		alphabet[i][let2num(words[i][j])] = alphabet[i][let2num(words[i][j])] + 1

numbers = [453, 272, 309, 218, 138, 377, 283, 283, 366, 454, 323, 320, 343, 200, 670, 275, 296, 489, 204, 606, 696, 166, 340, 273, 170, 397]

a = matrix(alphabet)
b = matrix([numbers]).transpose()
c = a\b
print(c)

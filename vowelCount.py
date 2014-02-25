from sys import argv

vowels = ['a','e','i','o','u','y']

def vowel_count(text,display):
	vowelhits = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
	count = 0
	for letter in text:
		if letter in vowels:
			count += 1
			if letter == 'a':
				vowelhits['a'] +=1
			elif letter == 'e':
				vowelhits['e'] +=1
			elif letter == 'i':
				vowelhits['i'] +=1
			elif letter == 'o':
				vowelhits['o'] +=1
			elif letter == 'u':
				vowelhits['u'] +=1
			elif letter == 'y':
				vowelhits['y'] +=1

	if display:
		print vowelhits
	return count

if __name__=="__main__":
	script, text = argv
	print vowel_count(text,True)


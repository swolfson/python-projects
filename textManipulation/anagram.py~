from sys import argv
import json
from itertools import permutations

os_dictionary = "/usr/share/dict/words"

script, command, targetword = argv
#part of the super inefficient way of doing things
def isword(target,wordbank=os_dictionary):
	all_words  = [line.strip() for line in open(os_dictionary)]
	valid_length = len(target)
	words_valid_length = []
	for word in all_words:
		if len(word) == valid_length:
			words_valid_length.append(word)
	if target in words_valid_length:
		return True
	else:
		return False

#part of the super inefficient function
def genPerms(target):
	perms = [x for x in permutations(target,len(target))]
	permfix = [''.join(item) for item in perms]
	return permfix

#don't use this; it is super inefficient
def genAnagrams(target,wordbank=os_dictionary):
	scramble = genPerms(target)
	anagrams = []
	for item in scramble:
		if isword(item,wordbank):
			anagrams.append(item)
	return anagrams

#creates a dict for fast anagram searching
def make_anagram_dictionary(wordbank=os_dictionary):
	all_words  = [line.strip() for line in open(wordbank)]
	print "dict loaded"
	i = -1
	anagram_dictionary = {}
	for word in all_words:
		i += 1
		print i
		k = "".join(sorted(word))
		if k in anagram_dictionary.keys():
			val = anagram_dictionary[k]
			anagram_dictionary[k] = val + ", " +  word
		else:
			anagram_dictionary[k] = word
		
	with open('anagram_dictionary.json','w') as f:
		json.dump(anagram_dictionary,f)
	print "dump complete"

def find_anagrams(targetword,andict='anagram_dictionary.json'):
	with open(andict) as f:
		anDict = json.load(f)
	word = "".join(sorted(targetword))
	return anDict[word]

if __name__=="__main__":
	if command == "make":
		make_anagram_dictionary()
	elif command == "find":
		print find_anagrams(targetword)
	else:
		print "command has to be either make or find"


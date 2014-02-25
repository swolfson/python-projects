from sys import argv

import string
#script, word, extra = argv

def reverse(targetstring):
	return targetstring[::-1]

if __name__=="__main__":
	script, target = argv
	print reverse(target)




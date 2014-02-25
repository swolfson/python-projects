from sys import argv

def latinize(targetword):
	first = targetword[0]
	return targetword[1::] + first + 'ay'

if __name__=="__main__":
	script, target = argv
	print latinize(target)



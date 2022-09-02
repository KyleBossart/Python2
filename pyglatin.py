# PygLatin - Python 2

first = raw_input("Enter a word:")
first = first.lower()
second = first[0]
third = first[1:]
final = third + second + "ay"
def pyg():
	if len(first) > 0 and first.isalpha():
		print final
	else:
		print "Please enter a valid word"
pyg()

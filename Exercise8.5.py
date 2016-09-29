"""
	Caesar cypher

	Lukas Merz 29.09.16

	Funzt bis zunere rotation fu 14.. nocher schiebder komischi zeiche inne
	

"""
def rotate_letter(letter,n):

	if letter.isupper():
		start = ord("A")
	elif letter.islower():
		start = ord("a")
	else:
		return letter

	numericLetter = ord(letter)
	end = start+26

	if numericLetter > end:
		numericLetter = numericLetter-end
	moved = chr(numericLetter+n)
	return moved
	
def rotate_word(word, n):
	i = 0

	for letter in word:
		cryptLetter = rotate_letter(letter,n)
		i = i+1
		print(end=cryptLetter)

	print("\n")	
	return

rotate_word("abbild", 14)

#zabcdefghijklmnopqrstuvwxy
#abcdefghijklmnopqrstuvwxyz

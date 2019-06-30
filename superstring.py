import random
from string import ascii_lowercase

TRIALS = 1000

class Tile: 
	def __init__(self, letter): 
		self.letter = letter
		if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'N' or letter == 'R' or letter == 'T' or letter == 'L' or letter == 'S' or letter == 'U':
			self.points = 1
		elif letter == 'D' or letter == 'G': 
			self.points = 2
		elif letter == 'B' or letter == 'C' or letter == 'M' or letter == 'P':
			self.points = 3
		elif letter == 'F' or letter == 'H' or letter == 'V' or letter == 'W' or letter == 'Y':
			self.points = 4
		elif letter == 'K': 
			self.points = 5
		elif letter == 'J' or letter == 'X':
			self.points = 8
		elif letter == 'Q' or letter == 'Z':
			self.points = 10
		elif letter == '?': 
			self.points = 0
		else: 
			print("Uh-oh")
	
	def printTile(self): 
		print(self.letter)
			
class Word: 
	def __init__(self, string): 
		self.tiles = []
		self.string = string.upper()
		for char in string.upper(): 
			self.tiles.append(Tile(char))
	
	def printWord(self): 
		print(self.string)
			
class Bag: 
	def __init__(self): 
		self.letters = []
		for i in range(12): 
			self.letters.append(Tile('E'))
		
		for i in range(9): 
			self.letters.append(Tile('A'))
			self.letters.append(Tile('I'))
			
		for i in range(8): 
			self.letters.append(Tile('O'))
		
		for i in range(6): 
			self.letters.append(Tile('N'))
			self.letters.append(Tile('R'))
			self.letters.append(Tile('T'))
			
		for i in range(4): 
			self.letters.append(Tile('L'))
			self.letters.append(Tile('S'))
			self.letters.append(Tile('U'))
			self.letters.append(Tile('D'))
			
		for i in range(2): 
			self.letters.append(Tile('G'))
			self.letters.append(Tile('B'))
			self.letters.append(Tile('C'))
			self.letters.append(Tile('M'))
			self.letters.append(Tile('P'))
			self.letters.append(Tile('F'))
			self.letters.append(Tile('H'))
			self.letters.append(Tile('V'))
			self.letters.append(Tile('W'))
			self.letters.append(Tile('Y'))
			self.letters.append(Tile('?'))
			
		self.letters.append(Tile('G'))
		self.letters.append(Tile('K'))
		self.letters.append(Tile('J'))
		self.letters.append(Tile('X'))
		self.letters.append(Tile('Q'))
		self.letters.append(Tile('Z'))
	
	def printBag(self): 
		for tile in self.letters: 
			tile.printTile()
			
	def shuffleLetters(self): 
		random.shuffle(self.letters)
	
	def randomSuperString(self): 
		self.shuffleLetters()
		superstring = ""
		for tile in self.letters: 
			superstring += tile.letter
		return superstring

def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in range(length):
    for j in range(i,length):
      alist.append(string[i:j + 1]) 
  return alist

def computeScore(word): 
	tmp = get_all_substrings(word)
	substrings = []
	scored_words = []
	score = 0
		
	for word in tmp: 
		substrings.append(Word(word))

	for word in substrings:
		if '?' not in word.string: 
			#if it's a real word we have not made yet
			if word.string.lower() in d and word.string.lower() not in scored_words:
				scored_words.append(word.string.lower())
				for tile in word.tiles:
					score += tile.points
		else: #word has a blank tile
			base = word.string[:-1] #remove the blank
			for c in ascii_lowercase: #add each letter of the alphabet and see if it is a word
				tmp = base + c
				if tmp.lower() in d and tmp.lower() not in scored_words: 
					scored_words.append(tmp.lower())
				for tile in word.tiles:
					score += tile.points
			
	#print(scored_words)		
	return score
	
def returnScore(tuple):
	return tuple[0]
	
	
f = open('scrabble_dict.txt', 'r')
dictionary = f.read().splitlines()
d = set(dictionary)

bag = Bag()
scores = []


for i in range(TRIALS): 
	str =  bag.randomSuperString()
	score = computeScore(str)
	scores.append((score, str))

scores.sort(reverse=True, key=returnScore)
for elem in scores: 
	print(elem)



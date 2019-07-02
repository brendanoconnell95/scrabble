import random
from string import ascii_lowercase

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
		self.tiles = []
		self.letters = []
		
		for i in range(12): 
			self.tiles.append(Tile('E'))
		
		for i in range(9): 
			self.tiles.append(Tile('A'))
			self.tiles.append(Tile('I'))
			
		for i in range(8): 
			self.tiles.append(Tile('O'))
		
		for i in range(6): 
			self.tiles.append(Tile('N'))
			self.tiles.append(Tile('R'))
			self.tiles.append(Tile('T'))
			
		for i in range(4): 
			self.tiles.append(Tile('L'))
			self.tiles.append(Tile('S'))
			self.tiles.append(Tile('U'))
			self.tiles.append(Tile('D'))
			
		for i in range(2): 
			self.tiles.append(Tile('G'))
			self.tiles.append(Tile('B'))
			self.tiles.append(Tile('C'))
			self.tiles.append(Tile('M'))
			self.tiles.append(Tile('P'))
			self.tiles.append(Tile('F'))
			self.tiles.append(Tile('H'))
			self.tiles.append(Tile('V'))
			self.tiles.append(Tile('W'))
			self.tiles.append(Tile('Y'))
			self.tiles.append(Tile('?'))
			
		self.tiles.append(Tile('G'))
		self.tiles.append(Tile('K'))
		self.tiles.append(Tile('J'))
		self.tiles.append(Tile('X'))
		self.tiles.append(Tile('Q'))
		self.tiles.append(Tile('Z'))
		
		for tile in self.tiles: 
			self.letters.append(tile.letter)
	
	def printBag(self): 
		for tile in self.tiles: 
			tile.printTile()
			
	def shuffleLetters(self): 
		random.shuffle(self.tiles)
	
	def randomSuperString(self): 
		self.shuffleLetters()
		superstring = ""
		for tile in self.tiles: 
			superstring += tile.letter
		return superstring
	
	def removeLetters(self, word): 
		#only remove letters once it is determined the word can be made
		good_letters = []
		tmp = self.letters[:]
		
		for char in word: 
			try: 
				tmp.remove(char.upper())
				good_letters.append(char.upper())
			except: 
				#print("no "+ char + "'s left")
				break
		
		
		if len(good_letters) == len(word): 
			for c in good_letters: 
				self.letters.remove(c)
			
			#remake self.tiles without the removed letters
			self.tiles = []
		
			for char in self.letters: 
				self.tiles.append(Tile(char))
				
			return True
		else: 
			return False
		
			
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
			blank_used = False
			for c in ascii_lowercase: #add each letter of the alphabet and see if it is a word
				tmp = word.string.replace("?",c)
				if tmp.lower() in d and tmp.lower() not in scored_words and not blank_used: 
					scored_words.append(tmp.lower())
					blank_used = True
					for tile in word.tiles:
						score += tile.points
			
	print(scored_words)		
	return score
	
def makeString(bag):
	dict_scores = scored_dict
	superstring = ""
	
	dict_scores.sort(reverse=True, key=sortScore)
	
	for i in range(len(dict_scores)): 
		word = dict_scores[i][1]
		if len(bag.letters) == 0: 
			break
		
		if bag.removeLetters(word): 
			superstring += word
			print("added", word)
		else: 
			pass
			
	score = computeScore(superstring)
	print(score, superstring)
	print(len(superstring))
	print(bag.letters)

def sortScore(tuple):
	return tuple[0]

def sortWord(tuple): 
	return tuple[1]
	
f = open('scrabble_dict.txt', 'r')
dictionary = f.read().splitlines()
d = set(dictionary)

sd = open('scored_dict.txt', 'r')
scored_dict = []

for i in sd.readlines(): 
	tmp = i.split()
	scored_dict.append((int(tmp[1]), tmp[0]))

	
bag = Bag()
scores = []
	
makeString(bag)







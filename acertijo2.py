charset = '123'
keylen = 21

# A vs B = 1
# A vs C = 2
# B vs C = 3

def checkAGames(games):
	if games.count("1") + games.count("2") == 10:
		return True
	else:
		return False

def checkBGames(games):
	if games.count("1") + games.count("3") == 15:
		return True
	else:
		return False

def checkCGames(games):
	if games.count("2") + games.count("3") == 17:
		return True
	else:
		return False

def recurse(width, position, baseString, returnDictionary):
	for char in charset:
		if(position < width - 1):
			if position > 0 and baseString[position - 1] == char:
				pass
			else:
				recurse(width, position + 1, baseString + char, returnDictionary)
		else:
			if position > 0 and baseString[position - 1] == char:
				pass	
			else:
				returnDictionary.append(baseString + char)

myDictionary = []

print "Generating dictionary"

recurse(keylen, 0, "", myDictionary) 

print "Dictionary generated. Calculating solutions"

for entry in myDictionary:
	if checkAGames(entry) and checkBGames(entry) and checkCGames(entry):
		print entry

import sys

class game:
	winner = ""
	loser = ""

	def __init__(self, winner, loser):
		self.winner = winner
		self.loser = loser
	
	def playgame(self, winner, loser):
		self.winner = winner
		self.loser = loser
	
	def printgame(self):
		print "Winner: " + self.winner + ", loser: " + self.loser + "\n"
	


def countgames(gamesplayed):
	score = {"A":0, "B":0, "C":0}

	if len(gamesplayed) == 0:
		return score

	for game in gamesplayed:
		score[game.winner]+=1
		score[game.loser]+=1
	
	return score

def missingPlayer(lastgame):
	players = lastgame.winner + lastgame.loser

	if "A" not in players:
		return "A"
	if "B" not in players:
		return "B"
	if "C" not in players:
		return "C"

def printGames(games):
	for game in games:
		game.printgame()

def solve(gamesplayed):

	score = countgames(gamesplayed)

	if (score["A"] == 10 and score["B"] == 15 and score["C"] == 17):
		print "Found solution!"
		printGames(gamesplayed)
		raw_input()
		
	if (score["A"] > 10 or score["B"] > 15 or score["C"] > 17):
		return []	
	
	if len(gamesplayed) > 0:
		lastgame = gamesplayed[-1]
		newPlayer = missingPlayer(lastgame)
		
		branches = []
		branches.append(game(lastgame.winner, newPlayer))
		branches.append(game(newPlayer, lastgame.winner))

		for branchgame in branches:
			gamesplayed.append(branchgame)
			branch = solve(gamesplayed)
			if len(branch) > 0:
				return branch
			gamesplayed.pop()

	if len(gamesplayed) == 0:
		branches = []
		branches.append(game("A", "B"))
		branches.append(game("A", "C"))
		branches.append(game("B", "A"))
		branches.append(game("B", "C"))
		branches.append(game("C", "A"))
		branches.append(game("C", "B"))
		
		for branchgame in branches:
			gamesplayed.append(branchgame)
			print "Exploring branch"
			branchgame.printgame()
			raw_input()
			branch = solve(gamesplayed)
			if len(branch) > 0:
				return branch
			gamesplayed.pop()

	return []

gamesplayed = []

solve(gamesplayed)

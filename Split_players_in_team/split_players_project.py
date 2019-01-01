from random import choice
file = open('biodata.txt', 'r')
players = file.read().splitlines()

teamA = []
teamB = []

while len(players)>0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    
    if players == []:
        break
    
    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)
    

print("Team A: ", teamA)
print("Team B: ", teamB)

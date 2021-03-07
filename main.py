from menu import initMenu
from game import playGame
from rules import showRules
from statistics import showStats
from player import getPlayerName, comparePlayers

print("\n\t Welcome to Rock, Paper, Scissors, and Saw\n")

player1Name = getPlayerName('first')
player2Name = getPlayerName('second')
stats = ''

if comparePlayers(player1Name, player2Name):
    player2Name = getPlayerName('second')

while True:
    initMenu()
    userSelection = input('Select an option: ')
    if userSelection == '4':
        break
    elif userSelection == '1':
        stats = playGame(player1Name, player2Name)
    elif userSelection == '2':
        showRules()
    elif userSelection == '3':
        showStats(player1Name, player2Name, stats)
    else:
        print("\t\nplease enter a valid selection\n")

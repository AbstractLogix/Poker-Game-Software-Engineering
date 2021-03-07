currentStats = [[]]


def showStats(player1Name, player2Name, stats):
    print('\tSTATS\n')
    if(stats == ''):
        print("\t\n Overall Winner: no rounds played yet\n")
        print("Player: ", player1Name, " Wins: 0 Losses: 0 Ties: 0\n")
        print("Player: ", player2Name, " Wins: 0 Losses: 0 Ties: 0\n")
    currentStats.append(player1Name)
    currentStats.append(player2Name)
    currentStats[currentStats].append(stats[0][0])
    currentStats.append(stats)
    print(overAllWinner(currentStats))

# 2-d array must be used to keep track of statistics
# each player's stats on a new line
# number of games each player one, lost, or had tie against the computer
# winner of the game is the one that won the most rounds out of the three rounds and lost the least number of rounds
# stats for each player will have his name and rounds and games stats will be shown on same line
# Statistics selection will display the overall human winner based on the most won games and lost least games against the computer compared to other human players.
# If both players had same number of wins and losses for games, a tie will be announced for the overall winner
# The statistics are accumulative until users exit the program
# on start all statistics are 0

    input("\nPress any enter to return to the menu ")
    return


def overAllWinner(currentstats):
    winner = currentStats
    print("\t\n Overall Winner: " + winner)

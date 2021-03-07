
def getPlayerName(player):
    playerName = input('\nWhat is the name of the ' + player + ' player? ')
    checkPlayer(playerName, player)
    return playerName


def checkPlayer(str, player):
    if (len(str) < 5) | (len(str) >= 20):
        print('please try again\n')
        getPlayerName(player)
    else:
        return

def comparePlayers(player1, player2):
    print("Player's cannot have the same names")
    return player1 == player2

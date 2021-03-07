import random


def playGame(player1Name, player2Name):
    return gameLoop(player1Name, player2Name)


def gameLoop(player1Name, player2Name):
    round = 1
    player1Record = []
    player2Record = []
    while round <= 3:
        print('\nWelcome to round: ' + str(round) + '\n')

        player1Selection = selection('one')
        player2Selection = selection('two')
        computerSelection = randomSelection()

        player1Record.append(
            playRound(player1Name, player1Selection, computerSelection))

        player2Record.append(
            playRound(player2Name, player2Selection, computerSelection))

        round += 1

    player1Stats = displayWinner(player1Name, player1Record)
    player2Stats = displayWinner(player2Name, player2Record)

    # returning overall records for stats
    return(player1Stats, player2Stats)

# TODO find the proper way to count and display the winner of the round e.g. record.count()


def displayWinner(player, record):
    print("\n\tGame Results")
    print("Player " + player + " record: ")

    wins = record.count(player)
    losses = record.count("computer")
    ties = record.count("ties")
    gameWinner = ''
    if((ties > wins) & (ties > losses)):
        gameWinner = 'Tied'
    if(wins > losses):
        gameWinner = wins
    if(losses > wins):
        gameWinner = losses

    print("Wins: ", wins, "Losses: ", losses, "Ties: ", ties)

    print("\n\t Winner is: ", gameWinner)

    return (player, wins, losses, ties)


def selection(player):
    playerSelection = input(
        'Player ' + player + ' make a selection: (1. rock, 2. paper, 3. scissors, or 4. saw) ')
    if playerSelection == '1':
        return 'rock'
    elif playerSelection == '2':
        return 'paper'
    elif playerSelection == '3':
        return 'scissors'
    elif playerSelection == '4':
        return 'saw'
    else:
        print('Invalid selection')
        selection(player)


def randomSelection():
    randomNum = random.randint(1, 4)
    if randomNum == 1:
        return 'rock'
    elif randomNum == 2:
        return 'paper'
    elif randomNum == 3:
        return 'scissors'
    elif randomNum == 4:
        return 'saw'

# rock > scissors , saw
# paper > rock
# scissor > paper
# saw > scissors , paper


def winner(playerName, playerSelection, computerSelection):

    if(((playerSelection == 'rock') & (computerSelection == 'scissors')) or ((playerSelection == 'scissors') & (computerSelection == 'paper'))
       or ((playerSelection == 'paper') & (computerSelection == 'rock')) or ((playerSelection == 'rock') & (computerSelection == 'saw'))
       or ((playerSelection == 'saw') & (computerSelection == 'scissors')) or ((playerSelection == 'saw') & (computerSelection == 'paper'))):
        return playerName
    elif(((playerSelection == 'rock') & (computerSelection == 'scissors')) or ((playerSelection == 'scissors') & (computerSelection == 'paper'))
         or ((playerSelection == 'paper') & (computerSelection == 'rock')) or ((playerSelection == 'rock') & (computerSelection == 'saw'))
            or ((playerSelection == 'saw') & (computerSelection == 'scissors')) or ((playerSelection == 'saw') & (computerSelection == 'paper'))):
        return 'Computer'
    else:
        return 'Tie'


def playRound(playerName, playerSelection, computerSelection):
    print("\nPlayer: " + playerName + " Selceted: " + playerSelection)
    print("Computer seleceted: " + computerSelection)
    theWinner = winner(playerName, playerSelection, computerSelection)
    print("Winner: " + theWinner + "\n")
    return theWinner

def showRules():
    print("\nWinner of the round will be determined as follow:"
          + "\n\ta.	Rock breaks scissors and Saw therefore rock wins over scissors and saw. Rock loses against paper."
          + "\n\tb.	Scissors cut paper therefore scissors win over paper. Scissors lose against rock and Saw."
          + "\n\tc.	Paper covers rock therefore paper wins over rock. Paper loses against scissors and saw."
          + "\n\td.	Saw cuts through scissors and paper therefore saw wins over scissors and paper. Saw loses against rock."
          + "\n\te.	If player and computer make the same selection, there is a tie."
          + "\n\n Winner of the game against the computer is one who won more rounds (must account for ties)."
          + "\n Overall human winner is based on the greater number of won games against the computer and least games lost (must account for tie between human players).")
    input("\nPress the enter key to return to the menu ")
    return

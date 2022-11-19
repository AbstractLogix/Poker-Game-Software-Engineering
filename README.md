# Software Design Specification

##### for

### Black Y Poker

### Version 1.0

### Prepared by Oscar Miranda

### 2/8/21

---

# Table of Contents

1. ### Introduction
   1. #### Purpose
   2. #### Document Conventions
   3. #### Intended Audience and Reading Suggestions
   4. #### Product Scope
   5. #### References
2. ### Overall Description
   1. #### Product Perspective
   2. #### Product Functions
   3. #### User Classes and Characteristics
   4. #### Operating Environment
   5. #### Design and Implementation Constraints 
   6. #### User Documentation 
   7. #### Assumptions and Dependencies 
3. ### External Interface Requirements 
   1. #### User Interfaces Overview 
   2. #### Hardware Interfaces 
   3. #### Software Interfaces 
4. ### Design Considerations
   1. #### Assumptions and Dependencies
   2. #### General Constraints
   3. #### Development Methods
5. ### System Architecture
   1. #### Architectural Strategies
   2. #### High level Overview of System Architecture
6. ### Human Interface Design
   1. #### Screen Images
   2. #### Screen Objects and Actions
7. ### Detailed System Design
   1. #### Data Structures
   2. #### Component 1 Name
   3. #### Component 2 Name
   4. #### Component 3 Name

### Appendix A: Glossary

---

# Revision History

| Name | Date | Reason For Changes | Version
| ----------- | ----------- | ----------- | ----------- |
| Oscar Miranda | 2/8/2021 | Initial commit | 1.0

---

# 1. Introduction

## 1.1 Purpose

The purpose of this Software Design Specification is to provide the design and implementation of a Poker game.

## 1.2 Document Conventions

Methods will be in bold along with a set of parentheses e.g., `print()`
The user is often referred to as the _player_ these are used interchangeably throughout the documentation.

## 1.3 Intended Audience and Reading Suggestions

This document is meant for developers and their project managers. It is recommended for developers to start with section 5 and proceed to section 7 for more a more in-depth view of the implementation of the modules. Project managers should start with section 5 and pay particular attention the high-level overview section.

## 1.4 Product Scope

## 1.4.1 Purpose

The software being specified is a stand-alone PC GUI based implementation of a poker game as specified by the customer, it is single player with the computer as a dealer.

## 1.4.2 High Level Flow

When the program starts, it prompts the user for their name. If the name exists in saved statistics, the program is then loaded with that information. If the name does not exist, then the player starts with 500 points. Then the main menu is displayed which has four selections:

1. Display rules
2. Show statistics
3. Play round
4. Exit

The display rules option displays all the rules for the game and how the player can win. The statistics selection displays the number of games a user has won and lost. The play round selection will allow the player to play a single round of the game. And the exit selection will end the program.

## 1.5 References

Black Y Poker SRS
Python documentation:
random _Generate pseudo-random numbers_ Python 3.9.1 documentation

---

# 2. Overall Description

## 2.1 Product Perspective

This a stand-alone software implementation of poker written to the specification provided by the customer and described in the Black Y Poker SRS.

## 2.2 Product Functions

The product must start the game by presenting the user with a prompt asking for their name in a GUI and then loading previous data if the name exists in its saved statistics memory. Then it presents a menu with the options for:

1. Display rules
2. Show statistics
3. Play round
4. Exit

Display rules will display the rules and how to win the game. Show statistics will show the wins and loses for the player.
Play round will allow the user to play a single round of poker with the computer acting as the dealer and the exit option will end the program.

## 2.3 User Classes and Characteristics

This software presumes that the users of this software are interested in playing a poker game and learning the rules.

## 2.4 Operating Environment

This software requires that the platform supports python 3. All major operating systems currently support python 3.

## 2.5 Design and Implementation Constraints

The program must be written in Python. It must be implemented using a procedural approach. The game must be called Black Y Poker and is a PC based GUI software system. The software implementation must be modular.

## 2.6 User Documentation

No user documentation is being shipped with the software. All existing documentation at this time is contained within this document and the SRS.

## 2.7 Assumptions and Dependencies

This specification assumes that python 3 is being used and installed on the host system and that the proper base libraries for python that include the random library, random _Generate pseudo-random numbers_ Python 3.9.1 documentation.

---

# 3. External Interface Requirements

## 3.1 User Interfaces Overview

The program has a GUI. When the program starts the user aka _player_ is prompted for their name and must enter a name up to 20 characters long containing any letter or digit.
If the name is too long or has incorrect characters an error message is displayed and the name that was typed in the prompt is cleared and the player must enter in another name, the player clicks OK to submit.
If the name exists in the saved statistics file, then the program is loaded with that plays wins and loses information.
If the name does not exist, then the player is brought to the main menu and begins with 500 points.
The menu is displayed with the following four options:

1.  Display rules
2.  Show statistics
3.  Play round
4.  Exit

The player can select any of the four options. The display rules option will display all the rules for the game and how the player can win.
The player can return to the menu by clicking OK. The statistics option will display the number of games the player has won and lost.
The player can return to the menu by clicking OK. The play round selection will allow the player to play a single round of the game.
Once the game is completed the player can return to the menu after clicking OK button. When the exit option is selected the program will end.
The GUI during the game will display the player's hand, his wins and losses, and the options for betting and the current bet.
Player will be presented with the BET5 and RAISE5 options for betting. The player continues to play until they are out of points.
A player also has the option to fold and to call _all in_.

## 3.2 Hardware Interfaces

The interactions between the software and the hardware are in the I/O from the clicks in the menu and in the game and keyboard of the user when entering their name at the start of the program. The saved statistics will also require I/O as it will be stored in a plain text file.

## 3.3 Software Interfaces

The software described in this document will need to interface with the host operating system's I/O. It will take keyboard and mouse click information from the player of the game and will store player statistics in a text file in statistics folder in the program's running directory.

---

# 4. Design Considerations

## 4.1 Assumptions and Dependencies

This software is designed to be run using python 3 and its operating system is irrelevant. Its only dependency will be to the python standard library, particularly its Random library.

## 4.2 General Constraints

The only constraint is the system where this program will run must have enough memory to facilitate the game�s player statistic file which keeps track of multiple players and their wins and losses. Any modern machine should not have an issue, but if this were deployed on a raspberry pi or Samsung smart fridge it would be a thing to consider.

## 4.3 Development Methods

Procedural programming focusing on a modular approach. There will be a main program with subroutines or functions.

---

# 5. System Architecture

## 5.1 Architectural Strategies

This software will be implemented using python 3 and its random library for randomizing the initial deck of cards from which the dealer deals. The player statistics will be saved in a text file called stats.txt in the same directory where the game is installed. The game will also read from this file and if it does not exist will create an empty one. Architecturally the view the player is given is separate from the program�s logic. i.e., the separation of the representation of information from the user�s interaction with it.

## 5.2 High level Overview of System Architecture

The game will have a few components made up of several functions. The first component is the gameInit() component which sets up the game by first calling the statsExists() function which checks to see if a stats.txt file exists.
If the file does not exist statsExists() will return false.
Then the gameInit() calls the playerInit() component it will call the function getPlayerName() which will prompt the player for their name.
playerInit() will call the findPlayer(String playerName) function which will return either true or false.
If true the playerInit() function will call the getPlayerStats(String playerName) function which returns the number of rounds won and lost by the player.
If false the playerInit() will call the addNewPlayer(String playerName) function that will create a new entry with the player's name and initialize their wins and losses to 0.
The playerInit() component then calls the mainMenu() component which will display the menu to the player this is the main game loop which will continue until the exit option is selected.
mainMenu() will hold all the previous information such as the player stats in memory and will have the option to display the rules which calls the displayRules() function.
The Show statistics options which calls the displayStats() function. The play round option which will call the playRound() component.
And finally exit will call the exit() function which ends the game loop and call the save() function which will save the player stats to the stats.txt file in the same directory where the game is installed.
If the file does not exist then the save() function will create it, this is known thanks to the gameInit() function which calls the statsExist() function at initialization of the game.

---

# 6. Human Interface Design

The player is first prompted to enter their name and the game will load that player�s previous statistics if they exist and if not, it will continue and display a menu with 4 options:

1. Display rules
2. Show statistics
3. Play round
4. Exit.

The user will select an option and will be able to return to the main menu by pressing OK on the screen of any of the menu options except the play round option which will only end when the player runs out of points or the dealer runs out of points signifying the end of a round.
During the play round option the player will have the option to BET5, RAISE5, MATCH, ALL IN, and FOLD.

## 6.1 Screen Images

screenshots
_coming soon_

## 6.2 Screen Objects and Actions

When the game begins the player is presented with a prompt text box asking for their name and a button to submit.
When the player presses the submit button the function that checks for their previous stats is called or if the name of the player does not exist the function that creates a new entry is called.
Then the player is presented with a menu which has the following four options:

1. Display rules, when this option is selected by the user by either licking or selecting the number one, the function that returns the rules as a String are displayed with the start screen menu background.
2. Show statistics, when this option is selected the statistics for the current player are displayed with the start screen menu background by calling the function getPlayerStats(String playerName) when the selection is made. It shows the number of wins and losses for the current player.
3. Play round, when this option is selected the playRound() function is called which starts a round of Black Y poker, which the player will play until they run out of points in which case they can return to the menu by pressing OK on the screen that is presented to them at the end of the round. Only one round is played at a time. During the round, the player is presented with five buttons: BET5, RAISE5, MATCH, ALL IN, and FOLD.BET5 places a bet of five points. RAISE5 increments the current bet by five. MATCH matches the current bet of the dealer. ALL IN bets all the players current points. FOLD will cause the round to end.
4. Exit, when this is selected the program ends by breaking out of its main loop.

---

# 7. Detailed System Design

## 7.1 Data Structures

`statsExist` Boolean representing if the stats.txt file exists already.
`playerName` holds player name in a string.
`playerExists` if a player exists or not in the stats.txt file.
`playerStats[]` array for player stats, wins, loses.
`deck[]` is stack that holds the deck of cards. Can only pop() off the top. 52 cards, cards from two to ten have corresponding values; Jack, Queen, King, and Ace have a value of 10.
`playerScore` holds the current points for the player.
`dealerScore` holds the current points for the dealer.

## 7.2 gameInit()

This component prepares the game to be played and its primary function is to check to see if the stats.txt exist and then call the playerInit() function.

## 7.2.1 Responsibilities

This component is responsible checking to see if the file required for the player stats exists e.g. stats.txt if not it will create a stats.txt file.

## 7.2.2 Uses/Interactions

This is an initial component and only interacts with the file system to check the existence of the stats.txt file.

## 7.2.3 Constraints

None.

## 7.2.4 Composition

This component calls the statsExists() function which checks for the stats.txt file and returns true if found or false if not i.e. Boolean.

## 7.2.5 Resources

This component does not depend on anything but the playerInit() component which is described next is dependent on the return value of this function which is a boolean value which is managed by this component by storing it in statsExist variable.

## 7.2.6 Processing

This component will attempt to access the stats.txt file by calling the statsExists() function which will search the current install directory for the stats.txt file and return either true if found or false if not.

## 7.3 playerInit()

This component prompts the user for their name and stores that value and calls additional functions to process this information.

## 7.3.1 Responsibilities

This component is responsible for processing the player�s initial input which is their name and will call the main game loop once the player�s stats are either loaded or initilizaed if this is the first time the player has played the game.

## 7.3.2 Uses/Interactions

This component prompts the user for their name and will perform the necessary processing and setup for the game to continue to the main menu.

## 7.3.3 Constraints

Requires the player to enter their name into the prompt.

## 7.3.4 Composition

This component calls several helper functions, `getPlayerName()` this function prompts the user for their name and returns it as a string.
`findPlayer(String playerName)` which will search for the player if it exists will return true and otherwise will return false if the name is not found.
The `playerInit()` function will call the `getPlayerStats(String playerName)` if `findPlayer()` was true and if not will call the `addNewPlayer(String playerName)` function which will create a new entry with player's name and initialize their wins and losses to 0.

## 7.3.5 Resources

This component depends on the user's input and the stats.txt file created by the gameInit() component.

## 7.3.6 Processing

This component calls the `getPlayerName()` helper function which prompts the user for their name and stores the returning string in a variable called playerName.
Then the helper function `findPlayer(String playerName)` is called taking as a parameter the playerName which the previous function returned and this searches for the name in the stats.txt file returning either true if found or false if not found and stores it in the playerExists Boolean variable.
If true then the helper function `getPlayerStats(String playerName)` is called which will return an array containing the player's name, number of wins, and number of losses.
If false the `playerInit()` function will call the `addNewPlayer(String playerName)` function which will create a new entry in the stats.txt file and initialize the wins and loses to 0. Then the `mainMenu()` component is called.

## 7.4 mainMenu()

This is the main game loop and displays the menu.

## 7.4.1 Responsibilities

This component displays the menu but is also the main game loop. The player will be able to select from the menu and continue to make selections until the exit selection is made from the main menu.

## 7.4.2 Uses/Interactions

This component has four functions that it calls when the user selects:

1.  `displayRules()`
2.  `displayStats()`
3.  `playRound()`
4.  `exit()`

## 7.4.3 Constraints

This component relies upon variables that were set previously like `playerStats[]`.

## 7.4.4 Composition

The subcomponent `displayRules()` displays the rules and allows the user to return to the main menu upon selecting OK.
The subcomponent `displayStats()` displays the `playerStats[]` in a readable format to the player and they can return to the main menu upon selecting OK.
The `playRound()` function allows the user to play a round of poker.
The `exit()` component exits the program and saves the player stats in the stats.txt file as a string with comma separated values e.g. name, wins, losses.

## 7.4.4.1 playRound()

This displays the game table and both the dealer, and the player get cards and the player's score is initialized to 500 points.
The deck is shuffled using the random python library and cards are popped off the top for both the player and the dealer to get cards.
The player starts by betting or folds or clicks all in.
When the player bets and the dealer bet those points are deducted or incremented at the end of the round depending on who wins.
`playerScore` and `dealerScore` hold these values are integers.
The Dealer responds to the player's moves.
The player and the dealer have options such as BET5 which bets 5 points, MATCH which matches the current bet,
`RAISE5` which raises the bet by 5 points, ALL IN which bets all the players current points and FOLD which ends the current players turn.
When the round starts only the BET5 and FOLD options will be active.
If the dealer raises then the MATCH, RAISE, and FOLD options will be active.
After each bet the pot value is increased and the player and dealer current points shown are decreased.
Once second betting is complete dealer cards are shown and the winner is announced.
The winner is decided by who has the bigger hand according to the rules and the classification of the hand that has the most value.
The dealer's behavior works as follows, if the dealer has a straight flush, four of a kind, flush, straight, or full house the dealer will not exchange any cards.
If the dealer has a three of a kind, he will exchange the other two cards. If the dealer has two pairs, he will exchange the other card.
If the dealer has one pair e will exchange the other three cards.
If the dealer has none of the above but has three or more cards of the same suit, he will not exchange any cards.
This continues until the player is out of points or the dealer has run out of points signifying the end of the round.

## 7.4.5 Resources

This components writes to the stats.txt upon exit() function being called which calls save() which is the helper function within exit that saves the current players stats to the stats.txt file.

## 7.4.6 Processing

Main menu component starts a do while loop that continues while the exit function has not been selected.
All the menu options call subcomponents which handle the display of information and the playing of the game.
This component holds the variables necessary to play the game such as the deck which is randomized by the random library and the player and dealer scores.
The game continues until the player's score is zero.

---

# Appendix A: Glossary

None.

Software Design Specification for Black Y Poker

import constants

def main():
    def cleandata():
        """
        This logic for the cleandata function loops through all elements in constants.py and determines if data needs to be cleaned,
        if data doesnt need to be cleaned it will copy the value from constants.py into empty cleanPlayerData list of dictionaries.
        """
        playerCount = 0
        for i in range(len(constants.PLAYERS)):
            playerCount = playerCount + 1

        cleanedPlayerData = [{} for i in range(playerCount)]
  
        for i in range(len(constants.PLAYERS)):
            for j in range(len(constants.PLAYERS[i])):
                if constants.PLAYERS[i][list(constants.PLAYERS[i].keys())[j]] == 'YES':
                    cleanedPlayerData[i][list(constants.PLAYERS[i].keys())[j]] = True
                elif constants.PLAYERS[i][list(constants.PLAYERS[i].keys())[j]] == 'NO':
                    cleanedPlayerData[i][list(constants.PLAYERS[i].keys())[j]] = False
                elif list(constants.PLAYERS[i].keys())[j] == 'height':
                    height = constants.PLAYERS[i][list(constants.PLAYERS[i].keys())[j]]
                    heightSplit = height.split(' ')
                    cleanedPlayerData[i][list(constants.PLAYERS[i].keys())[j]] = int(heightSplit[0])
                else:
                    cleanedPlayerData[i][list(constants.PLAYERS[i].keys())[j]] = constants.PLAYERS[i][list(constants.PLAYERS[i].keys())[j]]

        return cleanedPlayerData

   
    
    def playerBalance(x):
        teams = []
        playerNames = []
        players = cleandata()
        for i in range(len(constants.TEAMS)):
            teams.append(constants.TEAMS[i])

        n = int(len(players)/ len(teams))
        print(f"Player count: {n}")
        final = [players[i * n:(i + 1) * n] for i in range((len(players) + n - 1) // n )]
        for i in range(len(final[x])):
            playerNames.append(final[x][i]["name"])
        print(*playerNames, sep = ", ")
        
    def display():
        loop = True
        print("""BASKETBALL TEAM STATS TOOL

---- MENU ----

OPTIONS:
A) Display Team Stats
B) Quit""")
        while loop:
            userInput = input("Enter an option: ")
            if userInput == 'a' or userInput.upper() == 'A':
                print("""A) Panthers
B) Bandits
c) Warriors""")
                userInput2 = input("Enter an option: ")
                loop = False
                if userInput2 == 'a' or userInput2.upper() == 'A':
                    playerBalance(0)
                elif userInput2 == 'b' or userInput2.upper() == 'B':
                    playerBalance(1)
                elif userInput2 == 'c' or userInput2.upper() == 'C':
                    playerBalance(2)
            elif userInput == 'b' or userInput.upper() == 'B':
                quit()
            else: 
                print("Error please enter the options \"A\" or \"B\"")

    
        
          
    display()


if __name__ == "__main__":
    main()
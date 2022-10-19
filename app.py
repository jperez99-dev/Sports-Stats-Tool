import constants

def main():
    def cleandata():
        cleanplayerdata = {}



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
                cleandata()
                loop = False
            elif userInput == 'b' or userInput.upper() == 'B':
                quit()
            else: 
                print("Error please enter the options \"A\" or \"B\"")

    
        
        
        
    display()


if __name__ == "__main__":
    main()
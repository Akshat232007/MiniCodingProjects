
TicTacToeGrid = [
    [[1],[2],[3]],
    [[4],[5],[6]],
    [[7],[8],[9]]
]

def display_grid():
    for i in range(len(TicTacToeGrid)):
        print(f"{TicTacToeGrid[i]}")

PlayerNames = []

def set_player_names():
    Player1Name = input("Enter player 1 Name : ")
    Player2Name = input("Enter player 2 Name : ")
    PlayerNames.append(Player1Name)
    PlayerNames.append(Player2Name)

Round = 0
NoofRoundsuserneedtowin = 0
NoofRoundsuserneedtloose = 0

def SelectNofRounds():
    while True:
        InputRound = input("Enter No of rounds you want to play : ")
        if InputRound.isalpha():
            print("Rounds Shoulds be in numeric not alphabest!!.")
        elif InputRound.isnumeric():
            Round = int(InputRound)
            NoofRoundsuserneedtowin = (Round // 2) + 1
            NoofRoundsuserneedtloose = Round - NoofRoundsuserneedtowin
            print(f"To Win the Match You have to Win {NoofRoundsuserneedtowin} Rounds")
            break

def Player1Input_X():
    while True:
        pos = input("Enter Position you want to insert 'X' (1 - 9): ")

        if not pos.isnumeric():
            print("Invalid Position!, Position should be numeric not alphabets")
            continue

        pos = int(pos)

        if pos < 1 or pos > 9:
            print("Invalid Position!, Position should be in range of 1 to 9")
            continue

        row = (pos - 1) // 3
        col = (pos - 1) % 3

        if TicTacToeGrid[row][col][0] != 'X' and TicTacToeGrid[row][col][0] != 'O':
            TicTacToeGrid[row][col][0] = 'X'
            break
        else:
            print("Position is already Occupied!, Choose coorect position.")

def Player2Input_O():
    while True:
        pos = input("Enter Position you want to insert 'O' (1 - 9): ")

        if not pos.isnumeric():
            print("Invalid Position!, Position should be numeric not alphabets")
            continue

        pos = int(pos)

        if pos < 1 or pos > 9:
            print("Invalid Position!, Position should be in range of 1 to 9")
            continue

        row = (pos - 1) // 3
        col = (pos - 1) % 3

        if TicTacToeGrid[row][col][0] != 'X' and TicTacToeGrid[row][col][0] != 'O':
            TicTacToeGrid[row][col][0] = 'O'
            break
        else:
            print("Position is already Occupied!, Choose coorect position.")

        
def checkroundwinner():
    # Horizantal Checking
    if TicTacToeGrid[0][0][0] == TicTacToeGrid[0][1][0] == TicTacToeGrid[0][2][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
    
    elif TicTacToeGrid[1][0][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[1][2][0]:
        if TicTacToeGrid[1][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
    
    elif TicTacToeGrid[2][0][0] == TicTacToeGrid[2][1][0] == TicTacToeGrid[2][2][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
            print(f"The Winner of the match is : {PlayerNames[1]}")
    # Vertical Checking
    elif TicTacToeGrid[0][0][0] == TicTacToeGrid[1][0][0] == TicTacToeGrid[2][0][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
             
    elif TicTacToeGrid[0][1][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[2][1][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
             
    elif TicTacToeGrid[0][2][0] == TicTacToeGrid[1][2][0] == TicTacToeGrid[2][2][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
             
    #Diagonal Checking
    elif TicTacToeGrid[0][0][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[2][2][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
             
    elif TicTacToeGrid[0][2][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[2][0][0]:
        if TicTacToeGrid[0][0][0] is "X":
            print(f"The Winner of the match is : {PlayerNames[0]}")
        else:
             print(f"The Winner of the match is : {PlayerNames[1]}")
    
    
def StartGame():
    set_player_names()
    SelectNofRounds()

if __name__ == "__main__":
    print("-"*45)
    print("\n\tWelcome to Tic Tac Toe Game!!\t\n")
    print("-"*45)

    while True:
        print("\n" + " "*10 + "Game Menu" + " "*10 + "\n")
        print("1. Start New Game")
        print("2. Exit Game")

        choice = input("Enter your choice from above(1 or 2) : ")

        if choice.isalpha():
            print("The choice should be numeric not alphabets")
        elif choice.isnumeric() and int(choice) == 1:
            StartGame()
        elif choice.isnumeric() and int(choice) == 2:
            exit()
        else:
            print("Wrong Choice")

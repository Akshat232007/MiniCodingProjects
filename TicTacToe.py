
TicTacToeGrid = [
    [[1], [2], [3]],
    [[4], [5], [6]],
    [[7], [8], [9]]
]

PlayerNames = []

Round = 0
NoofRoundsuserneedtowin = 0
NoofRoundsuserneedtloose = 0


def reset_grid():
    global TicTacToeGrid

    TicTacToeGrid = [
        [[1], [2], [3]],
        [[4], [5], [6]],
        [[7], [8], [9]]
    ]


def display_grid():
    print()
    for i in range(len(TicTacToeGrid)):
        print(" | ".join(str(cell[0]) for cell in TicTacToeGrid[i]))
        if i < 2:
            print("--+---+--")
    print()


def set_player_names():
    PlayerNames.clear()

    Player1Name = input("Enter player 1 Name: ").strip()
    while not Player1Name:
        Player1Name = input("Player 1 name cannot be empty: ").strip()

    Player2Name = input("Enter player 2 Name: ").strip()
    while not Player2Name or Player2Name == Player1Name:
        Player2Name = input("Enter a different player 2 name: ").strip()

    PlayerNames.append(Player1Name)
    PlayerNames.append(Player2Name)


def SelectNofRounds():
    while True:
        InputRound = input("Enter No of rounds you want to play: ")

        if not InputRound.isnumeric() or int(InputRound) <= 0:
            print("Rounds should be a positive number!")
            continue

        Round = int(InputRound)

        if Round % 2 == 0:
            print("Please enter an odd number of rounds!")
            continue
        
        NoofRoundsuserneedtowin = (Round // 2) + 1
        NoofRoundsuserneedtloose = Round - NoofRoundsuserneedtowin

        print(f"To win the match, you have to win {NoofRoundsuserneedtowin} rounds.")

        return Round, NoofRoundsuserneedtowin, NoofRoundsuserneedtloose


def Player1Input_X():
    while True:
        pos = input("Enter Position you want to insert 'X' (1 - 9): ")

        if not pos.isnumeric():
            print("Invalid Position! Position should be numeric.")
            continue

        pos = int(pos)

        if pos < 1 or pos > 9:
            print("Invalid Position! Position should be in range of 1 to 9.")
            continue

        row = (pos - 1) // 3
        col = (pos - 1) % 3

        if TicTacToeGrid[row][col][0] not in ("X", "O"):
            TicTacToeGrid[row][col][0] = "X"
            break
        else:
            print("Position is already occupied! Choose another position.")


def Player2Input_O():
    while True:
        pos = input("Enter Position you want to insert 'O' (1 - 9): ")

        if not pos.isnumeric():
            print("Invalid Position! Position should be numeric.")
            continue

        pos = int(pos)

        if pos < 1 or pos > 9:
            print("Invalid Position! Position should be in range of 1 to 9.")
            continue

        row = (pos - 1) // 3
        col = (pos - 1) % 3

        if TicTacToeGrid[row][col][0] not in ("X", "O"):
            TicTacToeGrid[row][col][0] = "O"
            break
        else:
            print("Position is already occupied! Choose another position.")


def checkdraw():
    for i in range(len(TicTacToeGrid)):
        for j in range(len(TicTacToeGrid[i])):
            if TicTacToeGrid[i][j][0] not in ("X", "O"):
                return False

    return True


def checkroundwinner():
    # Horizontal Checking
    if TicTacToeGrid[0][0][0] == TicTacToeGrid[0][1][0] == TicTacToeGrid[0][2][0] and TicTacToeGrid[0][0][0] in ("X", "O"):
        winner = TicTacToeGrid[0][0][0]

    elif TicTacToeGrid[1][0][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[1][2][0] and TicTacToeGrid[1][0][0] in ("X", "O"):
        winner = TicTacToeGrid[1][0][0]

    elif TicTacToeGrid[2][0][0] == TicTacToeGrid[2][1][0] == TicTacToeGrid[2][2][0] and TicTacToeGrid[2][0][0] in ("X", "O"):
        winner = TicTacToeGrid[2][0][0]

    # Vertical Checking
    elif TicTacToeGrid[0][0][0] == TicTacToeGrid[1][0][0] == TicTacToeGrid[2][0][0] and TicTacToeGrid[0][0][0] in ("X", "O"):
        winner = TicTacToeGrid[0][0][0]

    elif TicTacToeGrid[0][1][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[2][1][0] and TicTacToeGrid[0][1][0] in ("X", "O"):
        winner = TicTacToeGrid[0][1][0]

    elif TicTacToeGrid[0][2][0] == TicTacToeGrid[1][2][0] == TicTacToeGrid[2][2][0] and TicTacToeGrid[0][2][0] in ("X", "O"):
        winner = TicTacToeGrid[0][2][0]

    # Diagonal Checking
    elif TicTacToeGrid[0][0][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[2][2][0] and TicTacToeGrid[0][0][0] in ("X", "O"):
        winner = TicTacToeGrid[0][0][0]

    elif TicTacToeGrid[0][2][0] == TicTacToeGrid[1][1][0] == TicTacToeGrid[2][0][0] and TicTacToeGrid[0][2][0] in ("X", "O"):
        winner = TicTacToeGrid[0][2][0]

    else:
        if checkdraw():
            print("The round is a draw!")
            return "Draw"

        return None

    if winner == "X":
        print(f"The Winner of the round is: {PlayerNames[0]}")
    else:
        print(f"The Winner of the round is: {PlayerNames[1]}")

    return winner


def play_round():
    reset_grid()
    current_player = 0

    while True:
        display_grid()

        if current_player == 0:
            Player1Input_X()
        else:
            Player2Input_O()

        result = checkroundwinner()

        if result is not None:
            display_grid()
            return result

        current_player = 1 - current_player


def StartGame():
    set_player_names()

    Round, NoofRoundsuserneedtowin, NoofRoundsuserneedtloose = SelectNofRounds()

    Player1Score = 0
    Player2Score = 0
    RoundsPlayed = 0

    while RoundsPlayed < Round:
        print(f"\n========== Round {RoundsPlayed + 1} ==========")

        result = play_round()
        RoundsPlayed += 1

        if result == "X":
            Player1Score += 1
        elif result == "O":
            Player2Score += 1

        print("\nCurrent Score:")
        print(f"{PlayerNames[0]}: {Player1Score}")
        print(f"{PlayerNames[1]}: {Player2Score}")

        if Player1Score == NoofRoundsuserneedtowin:
            print(f"\n{PlayerNames[0]} wins the match!")
            return

        elif Player2Score == NoofRoundsuserneedtowin:
            print(f"\n{PlayerNames[1]} wins the match!")
            return

    print("\nMatch Finished!")

    if Player1Score > Player2Score:
        print(f"{PlayerNames[0]} wins the match!")
    elif Player2Score > Player1Score:
        print(f"{PlayerNames[1]} wins the match!")
    else:
        print("The match is a draw!")


if __name__ == "__main__":
    while True:
        print("-" * 45)
        print("\n\tWelcome to Tic Tac Toe Game!!\t\n")
        print("-" * 45)

        print("\n1. Start New Game")
        print("2. Exit Game")

        choice = input("Enter your choice from above (1 or 2): ")

        if choice == "1":
            StartGame()

        elif choice == "2":
            print("Thanks for playing!")
            break

        else:
            print("Wrong Choice! Enter 1 or 2.")

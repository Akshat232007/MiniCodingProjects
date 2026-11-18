import random
import os

class ChessRules:

    @staticmethod
    def WPawnRule(row, col):
        if ChessGrid[row][col][0] == "wP":
            pass

    @staticmethod
    def WRookRule(row, col):
        if ChessGrid[row][col][0] == "wR":
            pass

    @staticmethod
    def WKnightRule(row, col):
        if ChessGrid[row][col][0] == "wN":
            pass

    @staticmethod
    def WBishopRule(row, col):
        if ChessGrid[row][col][0] == "wB":
            pass

    @staticmethod
    def WQuenRule(row, col):
        if ChessGrid[row][col][0] == "wQ":
            pass

    @staticmethod
    def WKingRule(row, col):
        if ChessGrid[row][col][0] == "wK":
            pass


Pieces = {
    "wR": "♜",
    "wN": "♞",
    "wB": "♝",
    "wQ": "♛",
    "wK": "♚",
    "wP": "♟",

    "bR": "♖",
    "bN": "♘",
    "bB": "♗",
    "bQ": "♕",
    "bK": "♔",
    "bP": "♙",

    1: 1,
    0: 0
}


ChessGrid = [
    [["bR"], ["bN"], ["bB"], ["bQ"], ["bK"], ["bB"], ["bN"], ["bR"]],
    [["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"]],
    [[1], [0], [1], [0], [1], [0], [1], [0]],
    [[0], [1], [0], [1], [0], [1], [0], [1]],
    [[1], [0], [1], [0], [1], [0], [1], [0]],
    [[0], [1], [0], [1], [0], [1], [0], [1]],
    [["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"]],
    [["wR"], ["wN"], ["wB"], ["wQ"], ["wK"], ["wB"], ["wN"], ["wR"]],
]


PlayerNames = []
Players = {}
CurrentPlayerSide = None
checkmate = False


def getPlayername():
    PlayerNames.clear()

    Player1Name = input("Enter player 1 Name: ").strip()
    while not Player1Name:
        Player1Name = input("Player 1 name cannot be empty: ").strip()

    Player2Name = input("Enter player 2 Name: ").strip()
    while not Player2Name or Player2Name == Player1Name:
        Player2Name = input("Enter a different player 2 name: ").strip()

    PlayerNames.append(Player1Name)
    PlayerNames.append(Player2Name)


def DisplayGrid():
    os.system("cls")

    print("White Pieces: ♜ Rook | ♞ Knight | ♝ Bishop | ♛ Queen | ♚ King | ♟ Pawn | 1 : White Block")
    print("Black Pieces: ♖ Rook | ♘ Knight | ♗ Bishop | ♕ Queen | ♔ King | ♙ Pawn | 0 : Black Block")
    print()

    print("   " + "".join(f"{chr(i):^7}" for i in range(ord("A"), ord("I"))))
    print("  +" + "+".join(["------"] * 8) + "+")

    for i in range(len(ChessGrid)):
        print(f"{i + 1} |", end="")

        for cell in ChessGrid[i]:
            print(f"{Pieces[cell[0]]:^6}|", end="")

        print()

        if i < 7:
            print("  +" + "+".join(["------"] * 8) + "+")

    print("  +" + "+".join(["------"] * 8) + "+")
    print()


def resetchessgrid():
    global ChessGrid

    ChessGrid = [
        [["bR"], ["bN"], ["bB"], ["bQ"], ["bK"], ["bB"], ["bN"], ["bR"]],
        [["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"]],
        [[1], [0], [1], [0], [1], [0], [1], [0]],
        [[0], [1], [0], [1], [0], [1], [0], [1]],
        [[1], [0], [1], [0], [1], [0], [1], [0]],
        [[0], [1], [0], [1], [0], [1], [0], [1]],
        [["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"]],
        [["wR"], ["wN"], ["wB"], ["wQ"], ["wK"], ["wB"], ["wN"], ["wR"]],
    ]



def WhitePlayerDine():
    global ChessGrid
    while True:
        try:
            selection = input("Enter Your Piece Selection (Ex: A 8): ").upper().split()

            if len(selection) != 2:
                print("Invalid input! Enter column and row.")
                continue

            col = ord(selection[0]) - 65
            row = int(selection[1]) - 1

            if not (0 <= row < 8 and 0 <= col < 8):
                print("Invalid coordinates! Choose A-H and 1-8.")
                continue

            if ChessGrid[row][col][0] not in (
                "wP", "wR", "wN", "wB", "wQ", "wK"
            ):
                print("Wrong Piece Selected! Choose White Pieces Only!")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Example: A 8")



def BlackPlayerDine():
    global ChessGrid

    while True:
        try:
            selection = input("Enter Your Piece Selection (Ex: A 1): ").upper().split()
            if len(selection) != 2:
                print("Invalid input! Enter column and row.")
                continue

            col = ord(selection[0]) - 65
            row = int(selection[1]) - 1

            if not (0 <= row < 8 and 0 <= col < 8):
                print("Invalid coordinates! Choose A-H and 1-8.")
                continue

            if ChessGrid[row][col][0] not in (
                "bP", "bR", "bN", "bB", "bQ", "bK"
            ):
                print("Wrong Piece Selected! Choose Black Pieces Only!")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Example: A 1")



def StartGame():
    global CurrentPlayerSide, checkmate

    getPlayername()
    resetchessgrid()
    Players.clear()

    Colors = [1, 0]
    random.shuffle(Colors)

    Players[PlayerNames[0]] = Colors[0]
    Players[PlayerNames[1]] = Colors[1]

    print("\nPlayer Color Assignment:")
    for name, color in Players.items():
        print(f"{name} : {'White' if color == 1 else 'Black'}")

    CurrentPlayerSide = 1

    print("\nWhite plays first!")    

    checkmate = False

    while not checkmate:
        for name, color in Players.items():
            if color == CurrentPlayerSide:
                print(f"\n{name}, it's your turn!")
                DisplayGrid()
                if color == 1:
                    row, col = WhitePlayerDine()
                else:
                    row, col = BlackPlayerDine()
                print(f"\nSelected Piece: "f"{Pieces[ChessGrid[row][col][0]]}")
                CurrentPlayerSide = 1 - CurrentPlayerSide
                break


if __name__ == "__main__":
    while True:
        print("_" * 45)
        print("\n\tWelcome to Chess Game!!\t\n")
        print("_" * 45)

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
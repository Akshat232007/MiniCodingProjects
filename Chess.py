import random
import os

class ChessRules:
    def WPawnRule(row,col):
        global ChessGrid
        
        if ChessGrid[row][col] == "wP":
            pass
        
    def WRookRule(row,col):
        global ChessGrid
        
        if ChessGrid[row][col] == "wR":
            pass
        
    def WKnightRule(row,col):
        global ChessGrid
        
        if ChessGrid[row][col] == "wN":
            pass
        
    def WBishopRule(row,col):
        global ChessGrid
        
        if ChessGrid[row][col] == "wB":
            pass
        
    def WQuenRule(row,col):
        global ChessGrid
        
        if ChessGrid[row,col] == "wQ":
            pass
        
    def WKingRule(row, col):
        global ChessGrid
        
        if ChessGrid[row,col] == "wK":
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

col = {
      
}



PlayerNames = []
Players = {}
CurrentPlayerSide = None
checkmate = None



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

    while CurrentPlayerSide == 1:
        row, col = map(input("Enter Your Piece Selection (Ex : A 8, space is needed!) : ").split())
            
        col = int(col)
        row = ascii(row) - 64
        
        if ChessGrid[row][col] not in ("wP", "wR", "wN", "wB", "wQ", "wK"):
            print("Wrong Piece Selected!, Choose White Pieces Only!")
        else:
            
            
            
            pass

def BlackPlayerDine():
    global ChessGrid

    while CurrentPlayerSide == 0:
        row, col = map(input("Enter Your Piece Selection (Ex : A 8, space is needed!) : ").split())
            
        col = int(col)
        row = ascii(row) - 64
        
        if ChessGrid[row][col] not in ("bP", "bR", "bN", "bB", "bQ", "bK"):
            print("Wrong Piece Selected!, Choose Black Pieces Only!")
        else:
            
            
            
            
            pass
    
    
     

def StartGame():
    global CurrentPlayerSide, checkmate

    getPlayername()
    resetchessgrid()

    Players.clear()

    Players[PlayerNames[0]] = None
    Players[PlayerNames[1]] = None

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
                if color == 1:
                    WhitePlayerDine()
                else:
                    BlackPlayerDine()
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
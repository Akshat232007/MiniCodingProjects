import random

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
    
    1 : 1,
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
Colors = []
CurrentPlayerSide = None

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


def StartGame():
    global CurrentPlayerSide
    getPlayername()
    resetchessgrid()

    Colors.clear()
    Colors.extend([1, 0])
    random.shuffle(Colors)

    print("\nPlayer Color Assignment:")
    print(f"{PlayerNames[0]} : {'White' if Colors[0] == 1 else 'Black'}")
    print(f"{PlayerNames[1]} : {'White' if Colors[1] == 1 else 'Black'}")

    CurrentPlayerSide = 1
    

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
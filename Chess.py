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
    
    "1" : 1,
    "0" : 0 
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


def DisplayGrid():
    print("White Pieces: ♜ Rook | ♞ Knight | ♝ Bishop | ♛ Queen | ♚ King | ♟ Pawn")
    print("Black Pieces: ♖ Rook | ♘ Knight | ♗ Bishop | ♕ Queen | ♔ King | ♙ Pawn")
    print()

    print("   " + "".join(f"{chr(i):^7}" for i in range(ord("A"), ord("I"))))
    print("  +" + "+".join(["------"] * 8) + "+")

    for i in range(len(ChessGrid)):
        print(f"{i + 1} |", end="")

        for cell in ChessGrid[i]:
            print(f"{Pieces[str(cell[0])]:^6}|", end="")

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
    
    
    DisplayGrid()
    


def StartGame():
    DisplayGrid()
    resetchessgrid()
    pass

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
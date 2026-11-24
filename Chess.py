
import random
import os
import copy

class ChessRules:
    @staticmethod
    def InsideBoard(row, col):
        return 0 <= row < 8 and 0 <= col < 8

    @staticmethod
    def GetPiece(row, col):
        piece = ChessGrid[row][col][0]
        if isinstance(piece, str):
            return piece
        return None

    @staticmethod
    def GetSide(piece):
        if piece is None:
            return None
        return 1 if piece[0] == "w" else 0

    @staticmethod
    def IsSquareAttacked(row, col, side):
        pawn_row = row + 1 if side == 1 else row - 1

        for pawn_col in (col - 1, col + 1):
            if ChessRules.InsideBoard(pawn_row, pawn_col):
                piece = ChessRules.GetPiece(pawn_row, pawn_col)
                if piece == ("wP" if side == 1 else "bP"):
                    return True

        KnightMoves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        for r, c in KnightMoves:
            nr, nc = row + r, col + c
            if ChessRules.InsideBoard(nr, nc):
                piece = ChessRules.GetPiece(nr, nc)
                if piece == ("wN" if side == 1 else "bN"):
                    return True

        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == 0 and c == 0:
                    continue

                nr, nc = row + r, col + c

                if ChessRules.InsideBoard(nr, nc):
                    piece = ChessRules.GetPiece(nr, nc)
                    if piece == ("wK" if side == 1 else "bK"):
                        return True

        Directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for dr, dc in Directions:
            nr, nc = row + dr, col + dc
            distance = 1

            while ChessRules.InsideBoard(nr, nc):
                piece = ChessRules.GetPiece(nr, nc)

                if piece is not None:
                    if ChessRules.GetSide(piece) == side:
                        if piece[1] == "Q":
                            return True

                        if distance == 1 and piece[1] == "K":
                            return True

                        if (dr == 0 or dc == 0) and piece[1] == "R":
                            return True

                        if abs(dr) == abs(dc) and piece[1] == "B":
                            return True

                    break

                nr += dr
                nc += dc
                distance += 1

        return False

    @staticmethod
    def IsInCheck(side):
        king = "wK" if side == 1 else "bK"

        for row in range(8):
            for col in range(8):
                if ChessRules.GetPiece(row, col) == king:
                    return ChessRules.IsSquareAttacked(row, col, 1 - side)

        return True

    @staticmethod
    def PawnRule(row, col):
        piece = ChessRules.GetPiece(row, col)
        side = ChessRules.GetSide(piece)

        direction = -1 if side == 1 else 1
        start_row = 6 if side == 1 else 1
        Possible_move = []

        next_row = row + direction

        if ChessRules.InsideBoard(next_row, col):
            if ChessRules.GetPiece(next_row, col) is None:
                Possible_move.append((next_row, col))

                if row == start_row:
                    double_row = row + (direction * 2)

                    if ChessRules.GetPiece(double_row, col) is None:
                        Possible_move.append((double_row, col))

        for dc in (-1, 1):
            nc = col + dc

            if ChessRules.InsideBoard(next_row, nc):
                target = ChessRules.GetPiece(next_row, nc)

                if target is not None and ChessRules.GetSide(target) != side:
                    Possible_move.append((next_row, nc))

                elif (next_row, nc) == EnPassantTarget:
                    Possible_move.append((next_row, nc))

        return Possible_move

    @staticmethod
    def RookRule(row, col):
        Possible_move = []
        side = ChessRules.GetSide(ChessRules.GetPiece(row, col))

        Directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in Directions:
            nr, nc = row + dr, col + dc

            while ChessRules.InsideBoard(nr, nc):
                target = ChessRules.GetPiece(nr, nc)

                if target is None:
                    Possible_move.append((nr, nc))
                else:
                    if ChessRules.GetSide(target) != side:
                        Possible_move.append((nr, nc))
                    break

                nr += dr
                nc += dc

        return Possible_move

    @staticmethod
    def KnightRule(row, col):
        Possible_move = []
        side = ChessRules.GetSide(ChessRules.GetPiece(row, col))

        Directions = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        for dr, dc in Directions:
            nr, nc = row + dr, col + dc

            if ChessRules.InsideBoard(nr, nc):
                target = ChessRules.GetPiece(nr, nc)

                if target is None or ChessRules.GetSide(target) != side:
                    Possible_move.append((nr, nc))

        return Possible_move

    @staticmethod
    def BishopRule(row, col):
        Possible_move = []
        side = ChessRules.GetSide(ChessRules.GetPiece(row, col))

        Directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in Directions:
            nr, nc = row + dr, col + dc

            while ChessRules.InsideBoard(nr, nc):
                target = ChessRules.GetPiece(nr, nc)

                if target is None:
                    Possible_move.append((nr, nc))
                else:
                    if ChessRules.GetSide(target) != side:
                        Possible_move.append((nr, nc))
                    break

                nr += dr
                nc += dc

        return Possible_move

    @staticmethod
    def QueenRule(row, col):
        return ChessRules.RookRule(row, col) + ChessRules.BishopRule(row, col)

    @staticmethod
    def KingRule(row, col):
        Possible_move = []
        side = ChessRules.GetSide(ChessRules.GetPiece(row, col))

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue

                nr, nc = row + dr, col + dc

                if ChessRules.InsideBoard(nr, nc):
                    target = ChessRules.GetPiece(nr, nc)

                    if target is None or ChessRules.GetSide(target) != side:
                        Possible_move.append((nr, nc))

        if ChessRules.IsInCheck(side):
            return Possible_move

        enemy = 1 - side
        king_row = 7 if side == 1 else 0

        if row != king_row or col != 4:
            return Possible_move

        if CastlingRights["wK" if side == 1 else "bK"]:
            if CastlingRights["wR" if side == 1 else "bR"]:
                if ChessRules.GetPiece(king_row, 7) == ("wR" if side == 1 else "bR"):
                    if all(ChessRules.GetPiece(king_row, c) is None for c in (5, 6)):
                        if not ChessRules.IsSquareAttacked(king_row, 5, enemy) and not ChessRules.IsSquareAttacked(king_row, 6, enemy):
                            Possible_move.append((king_row, 6))

            if CastlingRights["wL" if side == 1 else "bL"]:
                if ChessRules.GetPiece(king_row, 0) == ("wR" if side == 1 else "bR"):
                    if all(ChessRules.GetPiece(king_row, c) is None for c in (1, 2, 3)):
                        if not ChessRules.IsSquareAttacked(king_row, 3, enemy) and not ChessRules.IsSquareAttacked(king_row, 2, enemy):
                            Possible_move.append((king_row, 2))

        return Possible_move

    @staticmethod
    def GetPossibleMoves(row, col):
        piece = ChessRules.GetPiece(row, col)

        if piece is None:
            return []

        if piece[1] == "P":
            return ChessRules.PawnRule(row, col)
        elif piece[1] == "R":
            return ChessRules.RookRule(row, col)
        elif piece[1] == "N":
            return ChessRules.KnightRule(row, col)
        elif piece[1] == "B":
            return ChessRules.BishopRule(row, col)
        elif piece[1] == "Q":
            return ChessRules.QueenRule(row, col)
        elif piece[1] == "K":
            return ChessRules.KingRule(row, col)

        return []

    @staticmethod
    def GetLegalMoves(row, col):
        Possible_move = ChessRules.GetPossibleMoves(row, col)
        Legal_move = []
        side = ChessRules.GetSide(ChessRules.GetPiece(row, col))

        for nr, nc in Possible_move:
            saved_grid = copy.deepcopy(ChessGrid)
            saved_rights = CastlingRights.copy()
            saved_ep = EnPassantTarget

            MakeMove(row, col, nr, nc, "Q")

            if not ChessRules.IsInCheck(side):
                Legal_move.append((nr, nc))

            ChessGrid[:] = saved_grid
            CastlingRights.clear()
            CastlingRights.update(saved_rights)
            globals()["EnPassantTarget"] = saved_ep

        return Legal_move

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

def NewChessGrid():
    return [
        [["bR"], ["bN"], ["bB"], ["bQ"], ["bK"], ["bB"], ["bN"], ["bR"]],
        [["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"], ["bP"]],
        [[1], [0], [1], [0], [1], [0], [1], [0]],
        [[0], [1], [0], [1], [0], [1], [0], [1]],
        [[1], [0], [1], [0], [1], [0], [1], [0]],
        [[0], [1], [0], [1], [0], [1], [0], [1]],
        [["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"], ["wP"]],
        [["wR"], ["wN"], ["wB"], ["wQ"], ["wK"], ["wB"], ["wN"], ["wR"]]
    ]

ChessGrid = NewChessGrid()
PlayerNames = []
Players = {}
CurrentPlayerSide = None
checkmate = False
EnPassantTarget = None
HalfMoveClock = 0
CastlingRights = {
    "wK": True,
    "wR": True,
    "wL": True,
    "bK": True,
    "bR": True,
    "bL": True
}

def getPlayername():
    PlayerNames.clear()

    Player1Name = input("Enter player 1 Name: ").strip()

    while not Player1Name:
        Player1Name = input("Player 1 name cannot be empty: ").strip()

    Player2Name = input("Enter player 2 Name: ").strip()

    while not Player2Name or Player2Name.casefold() == Player1Name.casefold():
        Player2Name = input("Enter a different player 2 name: ").strip()

    PlayerNames.append(Player1Name)
    PlayerNames.append(Player2Name)

def DisplayGrid():
    os.system("cls" if os.name == "nt" else "clear")

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
    global ChessGrid, EnPassantTarget, HalfMoveClock

    ChessGrid = NewChessGrid()
    EnPassantTarget = None
    HalfMoveClock = 0

    CastlingRights.update({
        "wK": True,
        "wR": True,
        "wL": True,
        "bK": True,
        "bR": True,
        "bL": True
    })

def FormatPosition(row, col):
    return f"{chr(col + 65)} {row + 1}"

def GetPlayerSelection(side):
    while True:
        try:
            selection = input("Enter Your Piece Selection (Ex: A 8) or RESIGN: ").upper().split()

            if selection == ["RESIGN"]:
                return None

            if len(selection) != 2:
                print("Invalid input! Enter column and row.")
                continue

            if len(selection[0]) != 1 or selection[0] not in "ABCDEFGH":
                print("Invalid column! Choose A-H.")
                continue

            col = ord(selection[0]) - 65
            row = int(selection[1]) - 1

            if not (0 <= row < 8):
                print("Invalid row! Choose 1-8.")
                continue

            piece = ChessRules.GetPiece(row, col)

            if piece is None or ChessRules.GetSide(piece) != side:
                print("Wrong Piece Selected! Choose Your Own Pieces!")
                continue

            Legal_move = ChessRules.GetLegalMoves(row, col)

            if not Legal_move:
                print("This piece has no legal moves!")
                continue

            return row, col, Legal_move

        except ValueError:
            print("Invalid input! Example: A 8")

def GetDestination(Legal_move):
    print("\nAvailable Moves:")

    for row, col in Legal_move:
        print(FormatPosition(row, col), end=" | ")

    print("\n")

    while True:
        try:
            selection = input("Enter Destination: ").upper().split()

            if len(selection) != 2:
                print("Invalid input! Enter column and row.")
                continue

            if len(selection[0]) != 1 or selection[0] not in "ABCDEFGH":
                print("Invalid column!")
                continue

            col = ord(selection[0]) - 65
            row = int(selection[1]) - 1

            if not ChessRules.InsideBoard(row, col):
                print("Invalid coordinates!")
                continue

            if (row, col) not in Legal_move:
                print("Illegal move! Choose an available destination.")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Example: A 6")

def Promotion(side):
    while True:
        choice = input("Promote Pawn to (Q/R/B/N): ").upper().strip()

        if choice in ("Q", "R", "B", "N"):
            return ("w" if side == 1 else "b") + choice

        print("Invalid choice! Choose Q, R, B or N.")

def MakeMove(row, col, nr, nc, promotion="Q"):
    global EnPassantTarget, HalfMoveClock

    moving = ChessRules.GetPiece(row, col)
    captured = ChessRules.GetPiece(nr, nc)
    side = ChessRules.GetSide(moving)

    if moving[1] == "P" or captured is not None:
        HalfMoveClock = 0
    else:
        HalfMoveClock += 1

    if moving == "wK":
        CastlingRights["wK"] = False

    elif moving == "bK":
        CastlingRights["bK"] = False

    if moving == "wR":
        if (row, col) == (7, 0):
            CastlingRights["wL"] = False
        elif (row, col) == (7, 7):
            CastlingRights["wR"] = False

    elif moving == "bR":
        if (row, col) == (0, 0):
            CastlingRights["bL"] = False
        elif (row, col) == (0, 7):
            CastlingRights["bR"] = False

    if captured == "wR":
        if (nr, nc) == (7, 0):
            CastlingRights["wL"] = False
        elif (nr, nc) == (7, 7):
            CastlingRights["wR"] = False

    elif captured == "bR":
        if (nr, nc) == (0, 0):
            CastlingRights["bL"] = False
        elif (nr, nc) == (0, 7):
            CastlingRights["bR"] = False

    if moving[1] == "P" and (nr, nc) == EnPassantTarget and captured is None:
        captured_row = nr + 1 if side == 1 else nr - 1
        ChessGrid[captured_row][nc] = [1 if (captured_row + nc) % 2 == 0 else 0]

    if moving[1] == "K" and abs(nc - col) == 2:
        if nc == 6:
            rook_col = 7
            new_rook_col = 5
        else:
            rook_col = 0
            new_rook_col = 3

        rook = ChessGrid[row][rook_col][0]
        ChessGrid[row][new_rook_col] = [rook]
        ChessGrid[row][rook_col] = [1 if (row + rook_col) % 2 == 0 else 0]

    ChessGrid[nr][nc] = [moving]
    ChessGrid[row][col] = [1 if (row + col) % 2 == 0 else 0]

    EnPassantTarget = None

    if moving[1] == "P" and abs(nr - row) == 2:
        EnPassantTarget = ((row + nr) // 2, col)

    if moving[1] == "P" and nr in (0, 7):
        ChessGrid[nr][nc] = [promotion if len(promotion) == 2 else ("w" if side == 1 else "b") + promotion]

def GetAllLegalMoves(side):
    AllMoves = {}

    for row in range(8):
        for col in range(8):
            piece = ChessRules.GetPiece(row, col)

            if piece is not None and ChessRules.GetSide(piece) == side:
                moves = ChessRules.GetLegalMoves(row, col)

                if moves:
                    AllMoves[(row, col)] = moves

    return AllMoves

def GetPositionKey(side):
    board = tuple(
        tuple(cell[0] for cell in row)
        for row in ChessGrid
    )

    rights = tuple(sorted(CastlingRights.items()))

    return board, side, rights, EnPassantTarget

def StartGame():
    global CurrentPlayerSide, checkmate

    getPlayername()
    resetchessgrid()
    Players.clear()

    Colors = [1, 0]
    random.shuffle(Colors)

    Players[PlayerNames[0]] = Colors[0]
    Players[PlayerNames[1]] = Colors[1]

    PlayerByColor = {color: name for name, color in Players.items()}

    print("\nPlayer Color Assignment:")

    for name, color in Players.items():
        print(f"{name} : {'White' if color == 1 else 'Black'}")

    CurrentPlayerSide = 1
    checkmate = False

    print("\nWhite plays first!")
    input("\nPress ENTER to start the game...")

    PositionCount = {GetPositionKey(CurrentPlayerSide): 1}

    while not checkmate:
        DisplayGrid()

        name = PlayerByColor[CurrentPlayerSide]

        print(f"{name}, it's your turn!")
        print(f"Playing: {'White' if CurrentPlayerSide == 1 else 'Black'}")

        if ChessRules.IsInCheck(CurrentPlayerSide):
            print("\nCHECK! Your King is under attack!")

        AllMoves = GetAllLegalMoves(CurrentPlayerSide)

        if not AllMoves:
            if ChessRules.IsInCheck(CurrentPlayerSide):
                print("\nCHECKMATE!")
                print(f"{PlayerByColor[1 - CurrentPlayerSide]} WINS!")
            else:
                print("\nSTALEMATE! The game is a DRAW!")

            checkmate = True
            break

        selection = GetPlayerSelection(CurrentPlayerSide)

        if selection is None:
            print(f"\n{name} resigned!")
            print(f"{PlayerByColor[1 - CurrentPlayerSide]} WINS!")
            checkmate = True
            break

        row, col, Legal_move = selection

        print(f"\nSelected Piece: {Pieces[ChessGrid[row][col][0]]}")

        DisplayGrid()

        print(f"Available destinations for {FormatPosition(row, col)}:")

        nr, nc = GetDestination(Legal_move)

        moving = ChessRules.GetPiece(row, col)

        promotion = "Q"

        if moving[1] == "P" and nr in (0, 7):
            promotion = Promotion(CurrentPlayerSide)

        MakeMove(row, col, nr, nc, promotion)

        CurrentPlayerSide = 1 - CurrentPlayerSide

        PositionKey = GetPositionKey(CurrentPlayerSide)

        PositionCount[PositionKey] = PositionCount.get(PositionKey, 0) + 1

        if PositionCount[PositionKey] >= 3:
            DisplayGrid()
            print("DRAW! Threefold repetition.")
            checkmate = True

        elif HalfMoveClock >= 100:
            DisplayGrid()
            print("DRAW! Fifty-move rule.")
            checkmate = True

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

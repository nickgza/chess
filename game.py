from board import Board
from move import Move
import sys

class Game:
    board: Board
    white_score: float
    black_score: float
    white_player: str
    black_player: str

    def __init__(self):
        self.board = Board()
        self.white_score = 0
        self.black_score = 0
    
    def run_game(self):
        game_is_running = False
        manual_setup = False

        while True:
            try:
                line = input().split()
            except EOFError:
                break
            match line + [game_is_running]:
                case ['fen', False]:
                    manual_setup = True
                    self.board.setup_from_fen(input('Input valid FEN: '))
                    self.board.display()
                case ['game', False]:
                    if not manual_setup:
                        self.board.init()
                    game_is_running = True
                    self.board.display()
                case ['perft', False]:
                    if not manual_setup:
                        self.board.init()
                        self.board.display()
                    while True:
                        perft_line = input('Enter depth [and turn]: ').split()
                        if len(perft_line) > 2:
                            continue
                        elif len(perft_line) == 2:
                            depth, turn = perft_line
                        elif len(perft_line) == 0:
                            continue
                        else:
                            depth = perft_line[0]
                            turn = 'w'
                        if depth.startswith('q'):
                            break

                        try:
                            depth = int(depth)
                        except ValueError:
                            continue

                        if depth < 0:
                            continue

                        if turn not in 'wb':
                            continue
                        
                        ret = self.board.perft(depth, turn == 'w')
                        print(f'The number of positions after {depth}', 'move' if depth == 1 else 'moves', 'is', ret)
                        print(ret, file=sys.stderr)
                case ['move', *middle, True]:
                    start, end = middle[0], middle[1]
                    if len(middle) == 2:
                        move = Move(start, end)
                    else:
                        move = Move(start, end, middle[-1])
                    
                    if not self.board.board[start]:
                        print('There is no piece on', start)
                        continue
                    if self.board.board[start].is_white != self.board.white_turn:
                        print('You cannot move this piece')
                        continue
                    
                    if not self.board.board[start].is_legal(move, self.board):
                        print('Illegal move')
                        continue
                    
                    self.board.make_move(move)
                    self.board.display()
                case ['resign', True]:
                    game_is_running = False
                    manual_setup = False
                    if (self.board.white_turn):
                        self.black_score += 1
                        print('Black wins!')
                    else:
                        self.white_score += 1
                        print('White wins!')
                case _:
                    print('Invalid input')
                    continue
            if game_is_running:
                if self.board.white_turn:
                    white_mates = self.board.checkmate_stalemate_checked(self.board.WHITE)
                    if white_mates[0]:
                        print('Checkmate! Black wins!')
                        self.black_score += 1
                        game_is_running = False
                        manual_setup = False
                    elif white_mates[1]:
                        print('Stalemate!')
                        self.white_score += 0.5
                        self.black_score += 0.5
                        game_is_running = False
                        manual_setup = False
                    elif white_mates[2]:
                        print('White is in check.')
                else:
                    black_mates = self.board.checkmate_stalemate_checked(self.board.BLACK)
                    if black_mates[0]:
                        print('Checkmate! White wins!')
                        self.white_score += 1
                        game_is_running = False
                        manual_setup = False
                    elif black_mates[1]:
                        print('Stalemate!')
                        self.white_score += 0.5
                        self.black_score += 0.5
                        game_is_running = False
                        manual_setup = False
                    elif black_mates[2]:
                        print('Black is in check.')
                if self.board.insufficient_material():
                    print('Draw by insufficient material!')
                    self.white_score += 0.5
                    self.black_score += 0.5
                    game_is_running = False
                    manual_setup = False

    def print_score(self) -> None:
        print('Final score:')
        print(f'White: {self.white_score}')
        print(f'Black: {self.black_score}')

    def move_input(self, start: Move, end: Move) -> None | Move:
        if start == end:
            return None
            
        move = Move(start, end)
        
        if not self.board.board[start].is_legal(move, self.board):
            print('Illegal move')
            return None
        
        if self.board.board[start].piece_type == 'p':
            if self.board.board[start].is_white and end[1] == '8':
                return Move(start, end, '.')
            elif not self.board.board[start].is_white and end[1] == '1':
                return Move(start, end, '.')
        
        self.board.make_move(move)
        return move
    
    def valid_piece(self, start: Move) -> bool:
        if not self.board.board[start]:
            print('There is no piece on', start)
            return False
        if self.board.board[start].is_white != self.board.white_turn:
            print('You cannot move this piece')
            return False
        return True
    
    def checks(self) -> bool:
        if self.board.white_turn:
            white_mates = self.board.checkmate_stalemate_checked(self.board.WHITE)
            if white_mates[0]:
                print('Checkmate! Black wins!')
                self.black_score += 1
                return True
            elif white_mates[1]:
                print('Stalemate!')
                self.white_score += 0.5
                self.black_score += 0.5
                return True
            elif white_mates[2]:
                pass
        else:
            black_mates = self.board.checkmate_stalemate_checked(self.board.BLACK)
            if black_mates[0]:
                print('Checkmate! White wins!')
                self.white_score += 1
                return True
            elif black_mates[1]:
                print('Stalemate!')
                self.white_score += 0.5
                self.black_score += 0.5
                return True
            elif black_mates[2]:
                pass
        if self.board.insufficient_material():
            print('Draw by insufficient material!')
            self.white_score += 0.5
            self.black_score += 0.5
            return True

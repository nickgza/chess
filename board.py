from typing import Type
from piece import Piece
from move import Move
from itertools import chain

class Board:
    WHITE, BLACK = True, False
    squares = [
        'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
        'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
        'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
        'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
        'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
        'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
        'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
        'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
    ]
    white_turn = True
    en_passant: str
    white_king_square: str
    black_king_square: str
    white_king_side_castle: bool
    white_queen_side_castle: bool
    black_king_side_castle: bool
    black_queen_side_castle: bool
    board: dict[str, Type[Piece]]
    promoted_pawns: list[Type[Piece]]

    def __init__(self):
        self.board = {}
        self.promoted_pawns = []
        for square in self.squares:
            self.board[square] = None

    def display(self):
        print('Displaying board')

    def init(self):
        pieces = {
            'a1': (self.WHITE, 'r'),
            'b1': (self.WHITE, 'n'),
            'c1': (self.WHITE, 'b'),
            'd1': (self.WHITE, 'q'),
            'e1': (self.WHITE, 'k'),
            'f1': (self.WHITE, 'b'),
            'g1': (self.WHITE, 'n'),
            'h1': (self.WHITE, 'r'),
            'a2': (self.WHITE, 'p'),
            'b2': (self.WHITE, 'p'),
            'c2': (self.WHITE, 'p'),
            'd2': (self.WHITE, 'p'),
            'e2': (self.WHITE, 'p'),
            'f2': (self.WHITE, 'p'),
            'g2': (self.WHITE, 'p'),
            'h2': (self.WHITE, 'p'),
            'a7': (self.BLACK, 'p'),
            'b7': (self.BLACK, 'p'),
            'c7': (self.BLACK, 'p'),
            'd7': (self.BLACK, 'p'),
            'e7': (self.BLACK, 'p'),
            'f7': (self.BLACK, 'p'),
            'g7': (self.BLACK, 'p'),
            'h7': (self.BLACK, 'p'),
            'a8': (self.BLACK, 'r'),
            'b8': (self.BLACK, 'n'),
            'c8': (self.BLACK, 'b'),
            'd8': (self.BLACK, 'q'),
            'e8': (self.BLACK, 'k'),
            'f8': (self.BLACK, 'b'),
            'g8': (self.BLACK, 'n'),
            'h8': (self.BLACK, 'r'),
        }
        
        for square in self.squares:
            if square in pieces:
                self.board[square] = Piece(*pieces[square])
            else:
                self.board[square] = None

        self.white_king_square = 'e1'
        self.black_king_square = 'e8'
        self.white_king_side_castle = True
        self.white_queen_side_castle = True
        self.black_king_side_castle = True
        self.black_queen_side_castle = True
        self.white_turn = True
        self.en_passant = ''

    def clear(self):
        for square in self.squares:
            self.board[square] = None

    def setup_from_fen(self, fen):
        fen = fen.split()

        rank = '8'
        file = 'a'
        for c in fen.pop(0):
            square = file + rank
            match c:
                case '/':
                    rank = chr(ord(rank) - 1)
                    file = 'a'
                    continue
                case c if c.isalpha():
                    self.board[square] = Piece(self.BLACK if c.islower() else self.WHITE, c.lower())
                    if c == 'K':
                        self.white_king_square = square
                    elif c == 'k':
                        self.black_king_square = square
                case c if c.isnumeric():
                    n = ord(c) - ord('0')
                    for i in range(n):
                        self.board[file + rank] = None
                        file = chr(ord(file) + 1)
                    continue
            file = chr(ord(file) + 1)
        
        if fen.pop(0) == 'w':
            self.white_turn = True
        else:
            self.black_turn = True

        self.white_king_side_castle = False
        self.white_queen_side_castle = False
        self.black_king_side_castle = False
        self.black_queen_side_castle = False
        temp = fen.pop(0)
        if temp != '-':
            for c in temp:
                match c:
                    case 'K':
                        self.white_king_side_castle = True
                    case 'Q':
                        self.white_queen_side_castle = True
                    case 'k':
                        self.black_king_side_castle = True
                    case 'q':
                        self.black_queen_side_castle = True
        
        temp = fen.pop(0)
        if temp == '-':
            self.en_passant = ''
        else:
            self.en_passant = temp
    
    def to_fen(self):
        def chunk():
            for i in range(0, 64, 8):
                yield self.squares[i : i + 8]

        fen = []
        for rank in chunk():
            empty = 0
            row = []
            for square in rank:
                if self.board[square] == None:
                    empty += 1
                else:
                    if empty:
                        row.append(str(empty))
                        empty = 0
                    if self.board[square].is_white:
                        row.append(self.board[square].piece_type.upper())
                    else:
                        row.append(self.board[square].piece_type)
            if empty:
                row.append(str(empty))
            fen.append(''.join(row))
        
        fen = ['/'.join(fen)]

        fen.append(' ')
        if self.white_turn:
            fen.append('w')
        else:
            fen.append('b')
        
        can_castle = False
        fen.append(' ')
        if self.white_king_side_castle:
            can_castle = True
            fen.append('K')
        if self.white_queen_side_castle:
            can_castle = True
            fen.append('Q')
        if self.black_king_side_castle:
            can_castle = True
            fen.append('k')
        if self.black_queen_side_castle:
            can_castle = True
            fen.append('q')
        if not can_castle:
            fen.append('-')
        
        fen.append(' ')
        if self.en_passant:
            fen.append(self.en_passant)
        else:
            fen.append('-')
        
        return ''.join(fen)

    def make_move(self, move: Move):
        if self.board[move.end]:
            move.captured_type = self.board[move.end].piece_type
        else:
            move.captured_type = ' '

        # Castling
        if self.board[move.start].piece_type == 'k' and abs(ord(move.start_file()) - ord(move.end_file())) == 2:
            if move.start == 'e1':
                if move.end == 'c1':
                    self.board[move.start], self.board[move.end] = None, self.board[move.start]
                    self.board['a1'], self.board['d1'] = None, self.board['a1']
                elif move.end == 'g1':
                    self.board[move.start], self.board[move.end] = None, self.board[move.start]
                    self.board['h1'], self.board['f1'] = None, self.board['h1']
            elif move.start == 'e8':
                if move.end == 'c8':
                    self.board[move.start], self.board[move.end] = None, self.board[move.start]
                    self.board['a8'], self.board['d8'] = None, self.board['a8']
                elif move.end == 'g8':
                    self.board[move.start], self.board[move.end] = None, self.board[move.start]
                    self.board['h8'], self.board['f8'] = None, self.board['h8']
        else: # Normal move
            self.board[move.start], self.board[move.end] = None, self.board[move.start]

        moved_piece = self.board[move.end]

        # Promotion
        if moved_piece.piece_type == 'p':
            if moved_piece.is_white and move.end_rank() == '8':
                self.promoted_pawns.append(moved_piece)
                self.board[move.end] = Piece(self.WHITE, move.promote_to)
            elif not moved_piece.is_white and move.end_rank() == '1':
                self.promoted_pawns.append(moved_piece)
                self.board[move.end] = Piece(self.BLACK, move.promote_to)

        # En passant
        move.en_passant = self.en_passant
        if moved_piece.piece_type == 'p' and move.end == self.en_passant:
            if moved_piece.is_white:
                self.board[move.end_file() + chr(ord(move.end_rank()) - 1)] = None
            else:
                self.board[move.end_file() + chr(ord(move.end_rank()) + 1)] = None
        self.en_passant = ''
        if moved_piece.piece_type == 'p' and abs(ord(move.start_rank()) - ord(move.end_rank())) == 2:
            self.en_passant += move.end_file()
            if moved_piece.is_white:
                self.en_passant += chr(ord(move.end_rank()) - 1)
            else:
                self.en_passant += chr(ord(move.end_rank()) + 1)
        
        # Change king square
        if moved_piece.piece_type == 'k':
            if moved_piece.is_white:
                self.white_king_square = move.end
            else:
                self.black_king_square = move.end
        
        # Change castling availabilities
        move.affected_white_king_side_castle = False
        move.affected_white_queen_side_castle = False
        move.affected_black_king_side_castle = False
        move.affected_black_queen_side_castle = False
        if move.start == 'e1':
            if self.white_king_side_castle:
                move.affected_white_king_side_castle = True
            if self.white_queen_side_castle:
                move.affected_white_queen_side_castle = True
            self.white_king_side_castle, self.white_queen_side_castle = False, False
        if move.start == 'a1' or move.end == 'a1':
            if self.white_queen_side_castle:
                move.affected_white_queen_side_castle = True
            self.white_queen_side_castle = False
        if move.start == 'h1' or move.end == 'h1':
            if self.white_king_side_castle:
                move.affected_white_king_side_castle = True
            self.white_king_side_castle = False
        if move.start == 'e8':
            if self.black_king_side_castle:
                move.affected_black_king_side_castle = True
            if self.black_queen_side_castle:
                move.affected_black_queen_side_castle = True
            self.black_king_side_castle, self.black_queen_side_castle = False, False
        if move.start == 'a8' or move.end == 'a8':
            if self.black_queen_side_castle:
                move.affected_black_queen_side_castle = True
            self.black_queen_side_castle = False
        if move.start == 'h8' or move.end == 'h8':
            if self.black_king_side_castle:
                move.affected_black_king_side_castle = True
            self.black_king_side_castle = False
        
        self.white_turn = not self.white_turn

    def undo_move(self, move: Move):
        is_white = self.board[move.end].is_white
        piece_type = self.board[move.end].piece_type
        self.board[move.start], self.board[move.end] = self.board[move.end], self.board[move.start]

        self.en_passant = move.en_passant
        if move.end == self.en_passant:
            enemy_file = move.end_file()
            enemy_rank = chr(ord(move.end_rank()) - 1) if is_white else chr(ord(move.end_rank()) + 1)
            self.board[enemy_file + enemy_rank] = Piece(not is_white, 'p')
        
        if move.captured_type != ' ':
            self.board[move.end] = Piece(not is_white, move.captured_type)
        
        if move.promote_to != ' ':
            self.board[move.start] = Piece(is_white, 'p')

        if piece_type == 'k':
            if is_white:
                self.white_king_square = move.start
            else:
                self.black_king_square = move.start
        
        if piece_type == 'k' and abs(ord(move.start_file()) - ord(move.end_file())) == 2:
            if move.start == 'e1':
                if move.end == 'c1':
                    self.board['a1'], self.board['d1'] = self.board['d1'], self.board['a1']
                elif move.end == 'g1':
                    self.board['h1'], self.board['f1'] = self.board['f1'], self.board['h1']
            elif move.start == 'e8':
                if move.end == 'c8':
                    self.board['a8'], self.board['d8'] = self.board['d8'], self.board['a8']
                elif move.end == 'g8':
                    self.board['h8'], self.board['f8'] = self.board['f8'], self.board['h8']
        
        if move.affected_white_king_side_castle:
            self.white_king_side_castle = True
        if move.affected_white_queen_side_castle:
            self.white_queen_side_castle = True
        if move.affected_black_king_side_castle:
            self.black_king_side_castle = True
        if move.affected_black_queen_side_castle:
            self.black_queen_side_castle = True
        
        self.white_turn = not self.white_turn

    def square_is_attacked(self, target, attacking_colour):
        def attacked_by_line(d_file, d_rank):
            file = chr(ord(target[0]) + d_file)
            rank = chr(ord(target[1]) + d_rank)
            while file >= 'a' and file <= 'h' and rank >= '1' and rank <= '8':
                piece = self.board[file + rank]
                if piece:
                    if piece.is_white != attacking_colour:
                        return False
                    if piece.piece_type == 'q':
                        return True
                    if piece.piece_type == 'r' and d_file * d_rank == 0:
                        return True
                    if piece.piece_type == 'b' and abs(d_file * d_rank) == 1:
                        return True
                    return False
                file = chr(ord(file) + d_file)
                rank = chr(ord(rank) + d_rank)
            return False

        if (attacked_by_line(1, 0) or
            attacked_by_line(-1, 0) or
            attacked_by_line(0, 1) or
            attacked_by_line(0, -1) or
            attacked_by_line(1, 1) or
            attacked_by_line(-1, 1) or
            attacked_by_line(1, -1) or
            attacked_by_line(-1, -1)):
            return True
        
        knight_directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        for direction in knight_directions:
            file = chr(ord(target[0]) + direction[0])
            rank = chr(ord(target[1]) + direction[1])
            if file >= 'a' and file <= 'h' and rank >= '1' and rank <= '8':
                piece = self.board[file + rank]
                if piece and piece.is_white == attacking_colour and piece.piece_type == 'n':
                    return True
        
        around_directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        for direction in around_directions:
            file = chr(ord(target[0]) + direction[0])
            rank = chr(ord(target[1]) + direction[1])
            if file >= 'a' and file <= 'h' and rank >= '1' and rank <= '8':
                piece = self.board[file + rank]
                if piece and piece.is_white == attacking_colour:
                    if piece.piece_type == 'k':
                        return True
                    if piece.piece_type == 'p':
                        if attacking_colour == self.WHITE and abs(direction[0]) == 1 and direction[1] == -1:
                            return True
                        if attacking_colour == self.BLACK and abs(direction[0]) == 1 and direction[1] == 1:
                            return True
        return False

    def no_legal_moves(self, is_white):
        for square in self.squares:
            piece = self.board[square]
            if piece and piece.is_white == is_white:
                legal_moves = piece.generate_legal_moves(square, self)
                try:
                    next(legal_moves)
                except StopIteration:
                    return False
        return True

    def checkmate_stalemate_checked(self, attacked_colour: bool) -> tuple:
        king_square = self.white_king_square if attacked_colour == self.WHITE else self.black_king_square
        king_attacked = self.square_is_attacked(king_square, not attacked_colour)
        no_legal = self.no_legal_moves(attacked_colour)
        return (king_attacked and no_legal, not king_attacked and no_legal, king_attacked)
    
    def insufficient_material(self) -> bool:
        white_knight = 0
        black_knight = 0
        white_bishop = 0
        black_bishop = 0
        white_other = 0
        black_other = 0
        white_bishop_square = ''
        black_bishop_square = ''

        for square in self.squares:
            piece = self.board[square]
            if piece:
                if piece.is_white:
                    match piece.piece_type:
                        case 'n':
                            white_knight += 1
                        case 'b':
                            white_bishop += 1
                            white_bishop_square = square
                        case 'k':
                            pass
                        case _:
                            white_other += 1
                else:
                    match piece.piece_type:
                        case 'n':
                            black_knight += 1
                        case 'b':
                            black_bishop += 1
                            black_bishop_square = square
                        case 'k':
                            pass
                        case _:
                            black_other += 1
        
        if white_other + black_other == 0:
            if white_knight + black_knight + white_bishop + black_bishop == 0:
                return True
            if white_knight and black_knight + white_bishop + black_bishop == 0:
                return True
            if black_knight and white_knight + white_bishop + black_bishop == 0:
                return True
            if white_bishop == 1 and white_knight + black_knight + black_bishop == 0:
                return True
            if black_bishop == 1 and white_knight + black_knight + white_bishop == 0:
                return True
            if white_bishop == 1 and black_bishop == 1 and white_knight + black_knight == 0:
                return ((ord(white_bishop_square[0]) + ord(white_bishop_square[1])) % 2 ==
                        (ord(black_bishop_square[0]) + ord(black_bishop_square[1])) % 2)

    def display(self):
        hor = '\u2500'
        ver = '\u2502'
        four = '\u253c'
        down_right = '\u250c'
        down_left = '\u2510'
        up_right = '\u2514'
        up_left = '\u2518'
        right = '\u251c'
        left = '\u2524'
        down = '\u252c'
        up = '\u2534'

        def is_dark_square(file, rank):
            return (ord(file) - ord('a') + ord(rank) - ord('1')) % 2 == 0

        print(''.join([down_right, hor, 'a'] + [hor, down, hor] + ['b'] + [hor, down, hor] + ['c'] + [hor, down, hor] + ['d'] + [hor, down, hor] + ['e'] + [hor, down, hor] + ['f'] + [hor, down, hor] + ['g'] + [hor, down, hor] + ['h', hor, down_left]))
        for rank in '87654321':
            print(rank, end='')
            for file in 'abcdefgh':
                piece = self.board[file + rank]
                if piece is None:
                    if is_dark_square(file, rank):
                        print(f'   ', end='')
                    else:
                        print('   ', end='')
                else:
                    tp = piece.piece_type
                    if (piece.is_white):
                        tp = chr(ord(tp) + ord('A') - ord('a'))
                    print(f' {tp} ', end='')
                if file != 'h':
                    print(ver, end='')
            print(rank)
            if rank != '1':
                print(''.join([right] + [hor, hor, hor, four] * 7 + [hor, hor, hor, left]))
        
        print(''.join([up_right, hor, 'a'] + [hor, up, hor] + ['b'] + [hor, up, hor] + ['c'] + [hor, up, hor] + ['d'] + [hor, up, hor] + ['e'] + [hor, up, hor] + ['f'] + [hor, up, hor] + ['g'] + [hor, up, hor] + ['h', hor, up_left]))
    
    def perft(self, depth, white_turn, moves):
        if depth == 0:
            return 1
        
        all_moves = []
        for square in self.squares:
            if self.board[square] and self.board[square].is_white == white_turn:
                all_moves.append(self.board[square].generate_legal_moves(square, self))
        
        num_positions = 0
        for move in chain(*all_moves):
            # print(f'{self.to_fen()}    {move}    {moves}')
            self.make_move(move)
            num_positions += self.perft(depth - 1, not white_turn, moves + [move])
            self.undo_move(move)
        return num_positions

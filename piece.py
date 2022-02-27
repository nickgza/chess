from move import Move

class Piece:
    is_white: bool
    piece_type: str
    value: int

    def __init__(self, is_white, piece_type):
        self.is_white = is_white
        self.piece_type = piece_type
        match piece_type:
            case 'k':
                self.value = 0
            case 'q':
                self.value = 90
            case 'b':
                self.value = 30
            case 'n':
                self.value = 30
            case 'r':
                self.value = 50
            case 'p':
                self.value = 10
    
    def is_legal(self, move, board) -> bool:
        for generated_move in self.generate_legal_moves(move.start, board):
            if move == generated_move:
                return True
        return False
    
    def generate_legal_moves(self, start, board):
        for generated_move in self.generate_pseudo_legal_moves(start, board):
            if self.piece_type == 'k' and abs(ord(generated_move.start_file()) - ord(generated_move.end_file())) == 2:
                king_square = board.white_king_square if self.is_white else board.black_king_square
                if board.square_is_attacked(king_square, not self.is_white):
                    continue

                match generated_move.end:
                    case 'g1':
                        passing_square = 'f1'
                    case 'c1':
                        passing_square = 'd1'
                    case 'g8':
                        passing_square = 'f8'
                    case 'c8':
                        passing_square = 'd8'
                
                if board.square_is_attacked(passing_square, not self.is_white):
                    continue
                if board.square_is_attacked(generated_move.end, not self.is_white):
                    continue
                yield generated_move
            else:
                not_legal = False
                board.make_move(generated_move)
                king_square = board.white_king_square if self.is_white else board.black_king_square
                if board.square_is_attacked(king_square, not self.is_white):
                    not_legal = True
                board.undo_move(generated_move)
                if not_legal:
                    continue
                yield generated_move
    
    def generate_pseudo_legal_moves(self, start, board):
        def generate_moves_in_direction(d_file, d_rank):
            file = chr(ord(start[0]) + d_file)
            rank = chr(ord(start[1]) + d_rank)

            while file >= 'a' and file <= 'h' and rank >= '1' and rank <= '8':
                square = file + rank
                piece = board.board[square]
                if piece and self.is_white == piece.is_white:
                    break
                elif piece and self.is_white != piece.is_white:
                    yield Move(start, square)
                    break
                yield Move(start, square)
                
                file = chr(ord(file) + d_file)
                rank = chr(ord(rank) + d_rank)

        def add_move(d_file, d_rank):
            file = chr(ord(start[0]) + d_file)
            rank = chr(ord(start[1]) + d_rank)

            if (file < 'a' or file > 'h' or rank < '1' or rank > '8'):
                return
            square = file + rank
            piece = board.board[square]
            if not piece or self.is_white != piece.is_white:
                return Move(start, square)

        match self.piece_type:
            case 'r':
                yield from generate_moves_in_direction(1, 0)
                yield from generate_moves_in_direction(-1, 0)
                yield from generate_moves_in_direction(0, 1)
                yield from generate_moves_in_direction(0, -1)
            case 'b':
                yield from generate_moves_in_direction(1, 1)
                yield from generate_moves_in_direction(-1, 1)
                yield from generate_moves_in_direction(1, -1)
                yield from generate_moves_in_direction(-1, -1)
            case 'q':
                yield from generate_moves_in_direction(1, 0)
                yield from generate_moves_in_direction(-1, 0)
                yield from generate_moves_in_direction(0, 1)
                yield from generate_moves_in_direction(0, -1)
                yield from generate_moves_in_direction(1, 1)
                yield from generate_moves_in_direction(-1, 1)
                yield from generate_moves_in_direction(1, -1)
                yield from generate_moves_in_direction(-1, -1)
            case 'n':
                moves = []
                moves.append(add_move(1, 2))
                moves.append(add_move(2, 1))
                moves.append(add_move(2, -1))
                moves.append(add_move(1, -2))
                moves.append(add_move(-1, -2))
                moves.append(add_move(-2, -1))
                moves.append(add_move(-2, 1))
                moves.append(add_move(-1, 2))
                for m in moves:
                    if m is not None:
                        yield m
            case 'k':
                moves = []
                moves.append(add_move(1, 0))
                moves.append(add_move(-1, 0))
                moves.append(add_move(0, 1))
                moves.append(add_move(0, -1))
                moves.append(add_move(1, 1))
                moves.append(add_move(-1, 1))
                moves.append(add_move(1, -1))
                moves.append(add_move(-1, -1))
                for m in moves:
                    if m is not None:
                        yield m
                
                # Castling
                if self.is_white:
                    if board.white_king_side_castle and not board.board['f1'] and not board.board['g1']:
                        yield Move(start, 'g1')
                    if board.white_queen_side_castle and not board.board['d1'] and not board.board['c1'] and not board.board['b1']:
                        yield Move(start, 'c1')
                else:
                    if board.black_king_side_castle and not board.board['f8'] and not board.board['g8']:
                        yield Move(start, 'g8')
                    if board.black_queen_side_castle and not board.board['d8'] and not board.board['c8'] and not board.board['b8']:
                        yield Move(start, 'c8')
            case 'p':
                file, rank = start[0], start[1]
                forward = file
                forward2 = file
                promotion = False

                if self.is_white:
                    forward += chr(ord(rank) + 1)
                else:
                    forward += chr(ord(rank) - 1)
                if forward[1] in '18':
                    promotion = True

                if not (forward[1] in '12345678'):
                    print(forward, start, board.to_fen())
                
                if not board.board[forward]:
                    if promotion:
                        yield Move(start, forward, 'q')
                        yield Move(start, forward, 'r')
                        yield Move(start, forward, 'n')
                        yield Move(start, forward, 'b')
                    else:
                        yield Move(start, forward)
                if self.is_white and rank == '2':
                    forward2 += chr(ord(rank) + 2)
                elif not self.is_white and rank == '7':
                    forward2 += chr(ord(rank) - 2)
                if len(forward2) == 2:
                    if not board.board[forward] and not board.board[forward2]:
                        yield Move(start, forward2)
                if (file != 'a'):
                    left = chr(ord(forward[0]) - 1) + forward[1]
                    piece = board.board[left]
                    if (piece and self.is_white != piece.is_white) or left == board.en_passant:
                        if promotion:
                            yield Move(start, left, 'q')
                            yield Move(start, left, 'r')
                            yield Move(start, left, 'n')
                            yield Move(start, left, 'b')
                        else:
                            yield Move(start, left)
                if (file != 'h'):
                    right = chr(ord(forward[0]) + 1) + forward[1]
                    piece = board.board[right]
                    if (piece and self.is_white != piece.is_white) or right == board.en_passant:
                        if promotion:
                            yield Move(start, right, 'q')
                            yield Move(start, right, 'r')
                            yield Move(start, right, 'n')
                            yield Move(start, right, 'b')
                        else:
                            yield Move(start, right)

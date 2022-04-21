from game import Game
from move import Move
import time

def main_text():
    game = Game()
    game.run_game()
    game.print_score()

def main():
    import pygame as pg

    def calculate_top_left(width, height):
        if width > height:
            return ((width - height) // 2, 0)
        else:
            return (0, (height - width) // 2)

    def def_squares():
        size = pg.display.get_surface().get_size()
        dim = min(size)
        square_dim = round(dim / 8)
        top_left_x, top_left_y = calculate_top_left(*size)

        return {
            'a8': pg.Rect(top_left_x,                  top_left_y,                  square_dim, square_dim),
            'b8': pg.Rect(top_left_x + square_dim,     top_left_y,                  square_dim, square_dim),
            'c8': pg.Rect(top_left_x + 2 * square_dim, top_left_y,                  square_dim, square_dim),
            'd8': pg.Rect(top_left_x + 3 * square_dim, top_left_y,                  square_dim, square_dim),
            'e8': pg.Rect(top_left_x + 4 * square_dim, top_left_y,                  square_dim, square_dim),
            'f8': pg.Rect(top_left_x + 5 * square_dim, top_left_y,                  square_dim, square_dim),
            'g8': pg.Rect(top_left_x + 6 * square_dim, top_left_y,                  square_dim, square_dim),
            'h8': pg.Rect(top_left_x + 7 * square_dim, top_left_y,                  square_dim, square_dim),
            'a7': pg.Rect(top_left_x,                  top_left_y + square_dim,     square_dim, square_dim),
            'b7': pg.Rect(top_left_x + square_dim,     top_left_y + square_dim,     square_dim, square_dim),
            'c7': pg.Rect(top_left_x + 2 * square_dim, top_left_y + square_dim,     square_dim, square_dim),
            'd7': pg.Rect(top_left_x + 3 * square_dim, top_left_y + square_dim,     square_dim, square_dim),
            'e7': pg.Rect(top_left_x + 4 * square_dim, top_left_y + square_dim,     square_dim, square_dim),
            'f7': pg.Rect(top_left_x + 5 * square_dim, top_left_y + square_dim,     square_dim, square_dim),
            'g7': pg.Rect(top_left_x + 6 * square_dim, top_left_y + square_dim,     square_dim, square_dim),
            'h7': pg.Rect(top_left_x + 7 * square_dim, top_left_y + square_dim,     square_dim, square_dim),
            'a6': pg.Rect(top_left_x,                  top_left_y + 2 * square_dim, square_dim, square_dim),
            'b6': pg.Rect(top_left_x + square_dim,     top_left_y + 2 * square_dim, square_dim, square_dim),
            'c6': pg.Rect(top_left_x + 2 * square_dim, top_left_y + 2 * square_dim, square_dim, square_dim),
            'd6': pg.Rect(top_left_x + 3 * square_dim, top_left_y + 2 * square_dim, square_dim, square_dim),
            'e6': pg.Rect(top_left_x + 4 * square_dim, top_left_y + 2 * square_dim, square_dim, square_dim),
            'f6': pg.Rect(top_left_x + 5 * square_dim, top_left_y + 2 * square_dim, square_dim, square_dim),
            'g6': pg.Rect(top_left_x + 6 * square_dim, top_left_y + 2 * square_dim, square_dim, square_dim),
            'h6': pg.Rect(top_left_x + 7 * square_dim, top_left_y + 2 * square_dim, square_dim, square_dim),
            'a5': pg.Rect(top_left_x,                  top_left_y + 3 * square_dim, square_dim, square_dim),
            'b5': pg.Rect(top_left_x + square_dim,     top_left_y + 3 * square_dim, square_dim, square_dim),
            'c5': pg.Rect(top_left_x + 2 * square_dim, top_left_y + 3 * square_dim, square_dim, square_dim),
            'd5': pg.Rect(top_left_x + 3 * square_dim, top_left_y + 3 * square_dim, square_dim, square_dim),
            'e5': pg.Rect(top_left_x + 4 * square_dim, top_left_y + 3 * square_dim, square_dim, square_dim),
            'f5': pg.Rect(top_left_x + 5 * square_dim, top_left_y + 3 * square_dim, square_dim, square_dim),
            'g5': pg.Rect(top_left_x + 6 * square_dim, top_left_y + 3 * square_dim, square_dim, square_dim),
            'h5': pg.Rect(top_left_x + 7 * square_dim, top_left_y + 3 * square_dim, square_dim, square_dim),
            'a4': pg.Rect(top_left_x,                  top_left_y + 4 * square_dim, square_dim, square_dim),
            'b4': pg.Rect(top_left_x + square_dim,     top_left_y + 4 * square_dim, square_dim, square_dim),
            'c4': pg.Rect(top_left_x + 2 * square_dim, top_left_y + 4 * square_dim, square_dim, square_dim),
            'd4': pg.Rect(top_left_x + 3 * square_dim, top_left_y + 4 * square_dim, square_dim, square_dim),
            'e4': pg.Rect(top_left_x + 4 * square_dim, top_left_y + 4 * square_dim, square_dim, square_dim),
            'f4': pg.Rect(top_left_x + 5 * square_dim, top_left_y + 4 * square_dim, square_dim, square_dim),
            'g4': pg.Rect(top_left_x + 6 * square_dim, top_left_y + 4 * square_dim, square_dim, square_dim),
            'h4': pg.Rect(top_left_x + 7 * square_dim, top_left_y + 4 * square_dim, square_dim, square_dim),
            'a3': pg.Rect(top_left_x,                  top_left_y + 5 * square_dim, square_dim, square_dim),
            'b3': pg.Rect(top_left_x + square_dim,     top_left_y + 5 * square_dim, square_dim, square_dim),
            'c3': pg.Rect(top_left_x + 2 * square_dim, top_left_y + 5 * square_dim, square_dim, square_dim),
            'd3': pg.Rect(top_left_x + 3 * square_dim, top_left_y + 5 * square_dim, square_dim, square_dim),
            'e3': pg.Rect(top_left_x + 4 * square_dim, top_left_y + 5 * square_dim, square_dim, square_dim),
            'f3': pg.Rect(top_left_x + 5 * square_dim, top_left_y + 5 * square_dim, square_dim, square_dim),
            'g3': pg.Rect(top_left_x + 6 * square_dim, top_left_y + 5 * square_dim, square_dim, square_dim),
            'h3': pg.Rect(top_left_x + 7 * square_dim, top_left_y + 5 * square_dim, square_dim, square_dim),
            'a2': pg.Rect(top_left_x,                  top_left_y + 6 * square_dim, square_dim, square_dim),
            'b2': pg.Rect(top_left_x + square_dim,     top_left_y + 6 * square_dim, square_dim, square_dim),
            'c2': pg.Rect(top_left_x + 2 * square_dim, top_left_y + 6 * square_dim, square_dim, square_dim),
            'd2': pg.Rect(top_left_x + 3 * square_dim, top_left_y + 6 * square_dim, square_dim, square_dim),
            'e2': pg.Rect(top_left_x + 4 * square_dim, top_left_y + 6 * square_dim, square_dim, square_dim),
            'f2': pg.Rect(top_left_x + 5 * square_dim, top_left_y + 6 * square_dim, square_dim, square_dim),
            'g2': pg.Rect(top_left_x + 6 * square_dim, top_left_y + 6 * square_dim, square_dim, square_dim),
            'h2': pg.Rect(top_left_x + 7 * square_dim, top_left_y + 6 * square_dim, square_dim, square_dim),
            'a1': pg.Rect(top_left_x,                  top_left_y + 7 * square_dim, square_dim, square_dim),
            'b1': pg.Rect(top_left_x + square_dim,     top_left_y + 7 * square_dim, square_dim, square_dim),
            'c1': pg.Rect(top_left_x + 2 * square_dim, top_left_y + 7 * square_dim, square_dim, square_dim),
            'd1': pg.Rect(top_left_x + 3 * square_dim, top_left_y + 7 * square_dim, square_dim, square_dim),
            'e1': pg.Rect(top_left_x + 4 * square_dim, top_left_y + 7 * square_dim, square_dim, square_dim),
            'f1': pg.Rect(top_left_x + 5 * square_dim, top_left_y + 7 * square_dim, square_dim, square_dim),
            'g1': pg.Rect(top_left_x + 6 * square_dim, top_left_y + 7 * square_dim, square_dim, square_dim),
            'h1': pg.Rect(top_left_x + 7 * square_dim, top_left_y + 7 * square_dim, square_dim, square_dim),
        }

    def draw_squares(squares):
        for key, val in squares.items():
            pg.draw.rect(WIN, colours['DARK' if (ord(key[0]) + ord(key[1])) % 2 == 0 else 'LIGHT'], val)
    
    def highlight_last_move(squares, move):
        if move is not None:
            pg.draw.rect(WIN, colours['DARK_HIGHLIGHT' if (ord(move.start[0]) + ord(move.start[1])) % 2 == 0 else 'LIGHT_HIGHLIGHT'], squares[move.start])
            pg.draw.rect(WIN, colours['DARK_HIGHLIGHT' if (ord(move.end[0]) + ord(move.end[1])) % 2 == 0 else 'LIGHT_HIGHLIGHT'], squares[move.end])
    
    def highlight_selected(squares, square):
        if square is not None:
            pg.draw.rect(WIN, colours['DARK_HIGHLIGHT' if (ord(square[0]) + ord(square[1])) % 2 == 0 else 'LIGHT_HIGHLIGHT'], squares[square])

    def def_images():
        size = pg.display.get_surface().get_size()
        dim = min(size)
        square_dim = round(dim / 8)
        return {
            'K': pg.transform.smoothscale(orig_images['K'], (square_dim, square_dim)),
            'Q': pg.transform.smoothscale(orig_images['Q'], (square_dim, square_dim)),
            'R': pg.transform.smoothscale(orig_images['R'], (square_dim, square_dim)),
            'B': pg.transform.smoothscale(orig_images['B'], (square_dim, square_dim)),
            'N': pg.transform.smoothscale(orig_images['N'], (square_dim, square_dim)),
            'P': pg.transform.smoothscale(orig_images['P'], (square_dim, square_dim)),
            'k': pg.transform.smoothscale(orig_images['k'], (square_dim, square_dim)),
            'q': pg.transform.smoothscale(orig_images['q'], (square_dim, square_dim)),
            'r': pg.transform.smoothscale(orig_images['r'], (square_dim, square_dim)),
            'b': pg.transform.smoothscale(orig_images['b'], (square_dim, square_dim)),
            'n': pg.transform.smoothscale(orig_images['n'], (square_dim, square_dim)),
            'p': pg.transform.smoothscale(orig_images['p'], (square_dim, square_dim)),
        }

    def draw_pieces(squares, images, board):
        for square in squares:
            if board.board[square]:
                tp = board.board[square].piece_type
                WIN.blit(images[tp.upper() if board.board[square].is_white else tp], squares[square])
    
    def highlight_available(squares, square_selected: str, board):
        if square_selected is None:
            return
        for move in board.board[square_selected].generate_legal_moves(square_selected, board):
            rect = squares[move.end]
            if board.board[move.end] is None:
                pg.draw.circle(WIN2, (0, 0, 0, 60), tuple(map(lambda x: x*WIN2_FACTOR, rect.center)), rect.w / 6 * WIN2_FACTOR)
            else:
                pg.draw.circle(WIN2, (0, 0, 0, 60), tuple(map(lambda x: x*WIN2_FACTOR, rect.center)), rect.w / 2 * 0.96 * WIN2_FACTOR, int(rect.w / 13 * WIN2_FACTOR))
    
    def highlight_promotion(squares, promoting: str):
        file = promoting[0]
        if promoting[1] == '8':
            for rank, piece in zip('8765', 'QNRB'):
                pg.draw.rect(WIN, colours['WHITE'], squares[file + rank])
                WIN.blit(images[piece], squares[file + rank])
        elif promoting[1] == '1':
            for rank, piece in zip('1234', 'qnrb'):
                pg.draw.rect(WIN, colours['WHITE'], squares[file + rank])
                WIN.blit(images[piece], squares[file + rank])
    
    def calculate_promote_to(promoting: str, square_clicked: str) -> str:
        if promoting[0] == square_clicked[0]:
            if promoting[1] == '8':
                match square_clicked[1]:
                    case '8':
                        return 'q'
                    case '7':
                        return 'n'
                    case '6':
                        return 'r'
                    case '5':
                        return 'b'
            elif promoting[1] == '1':
                match square_clicked[1]:
                    case '1':
                        return 'q'
                    case '2':
                        return 'n'
                    case '3':
                        return 'r'
                    case '4':
                        return 'b'
        return ' '

    WIDTH, HEIGHT = 520, 520
    WIN = pg.display.set_mode((WIDTH, HEIGHT), pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE)
    WIN2 = pg.surface.Surface((WIDTH, HEIGHT), pg.SRCALPHA | pg.RESIZABLE)
    pg.display.set_caption('Chess')
    FPS = 60

    colours = {
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255),
        'LIGHT': (240, 217, 181),
        'DARK': (181, 136, 99),
        'LIGHT_HIGHLIGHT': (240, 240, 105),
        'DARK_HIGHLIGHT': (200, 183, 20),
    }

    orig_images = {
        'K': pg.image.load('assets/wk.png'),
        'Q': pg.image.load('assets/wq.png'),
        'R': pg.image.load('assets/wr.png'),
        'B': pg.image.load('assets/wb.png'),
        'N': pg.image.load('assets/wn.png'),
        'P': pg.image.load('assets/wp.png'),
        'k': pg.image.load('assets/bk.png'),
        'q': pg.image.load('assets/bq.png'),
        'r': pg.image.load('assets/br.png'),
        'b': pg.image.load('assets/bb.png'),
        'n': pg.image.load('assets/bn.png'),
        'p': pg.image.load('assets/bp.png'),
    }

    game = Game()
    game.board.init()

    run = True
    clock = pg.time.Clock()
    square_selected = None
    pending_deselect = None
    last_move = None
    promoting = None

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    run = False
                case pg.MOUSEBUTTONDOWN:
                    square_clicked = None
                    pos = pg.mouse.get_pos()
                    for square, rect in squares.items():
                        if rect.collidepoint(pos):
                            square_clicked = square
                            break
                    
                    if square_clicked is None:
                        continue
                    
                    if promoting is not None:
                        promote_to = calculate_promote_to(promoting, square_clicked)
                        if promote_to == ' ':
                            pass
                        else:
                            move = Move(square_selected, promoting, promote_to)
                            game.board.make_move(move)
                            last_move = move
                        square_selected = None
                        promoting = None
                    elif square_selected is None:
                        if game.valid_piece(square_clicked):
                            square_selected = square_clicked
                    elif square_selected == square_clicked:
                        pending_deselect = square_selected
                    elif game.board.board[square_clicked] is not None and game.board.board[square_clicked].is_white == game.board.white_turn:
                        square_selected = square_clicked
                    else:
                        move = game.move_input(square_selected, square_clicked)
                        if isinstance(move, str):
                            promoting = move
                            continue
                        square_selected = None
                        if move is not None:
                            last_move = move
                    
                case pg.MOUSEBUTTONUP:
                    square_clicked = None
                    pos = pg.mouse.get_pos()
                    for square, rect in squares.items():
                        if rect.collidepoint(pos):
                            square_clicked = square
                            break
                    
                    if pending_deselect is not None and square_clicked == pending_deselect:
                        square_selected = None
                        pending_deselect = None
                        continue
                    
                    if square_clicked is None or square_clicked == square_selected:
                        continue
                    
                    if square_selected is not None:
                        move = game.move_input(square_selected, square_clicked)
                        if isinstance(move, str):
                            promoting = move
                            continue
                        if move is not None:
                            square_selected = None
                            last_move = move
        
        WIN.fill(colours['BLACK'])

        squares = def_squares()
        draw_squares(squares)
        highlight_last_move(squares, last_move)
        highlight_selected(squares, square_selected)
        images = def_images()
        draw_pieces(squares, images, game.board)
        WIN2_FACTOR = 3
        WIN2 = pg.transform.scale(WIN2, tuple(map(lambda x: x*WIN2_FACTOR, pg.display.get_surface().get_size())))
        WIN2.fill((0, 0, 0, 0))
        if promoting is None:
            highlight_available(squares, square_selected, game.board)
        else:
            highlight_promotion(squares, promoting)

        WIN2 = pg.transform.smoothscale(WIN2, tuple(map(lambda x: x/WIN2_FACTOR, WIN2.get_size())))
        WIN.blit(WIN2, (0, 0))
        pg.display.flip()
        game_over = game.checks()
        if game_over:
            time.sleep(1)
            break
    
    game.print_score()
    pg.quit()


if __name__ == '__main__':
    # main_text()
    main()

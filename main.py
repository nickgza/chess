from game import Game

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

    def def_images():
        size = pg.display.get_surface().get_size()
        dim = min(size)
        square_dim = round(dim / 8)
        return {
            'K': pg.transform.smoothscale(pg.image.load('assets/wk.png'), (square_dim, square_dim)),
            'Q': pg.transform.smoothscale(pg.image.load('assets/wq.png'), (square_dim, square_dim)),
            'R': pg.transform.smoothscale(pg.image.load('assets/wr.png'), (square_dim, square_dim)),
            'B': pg.transform.smoothscale(pg.image.load('assets/wb.png'), (square_dim, square_dim)),
            'N': pg.transform.smoothscale(pg.image.load('assets/wn.png'), (square_dim, square_dim)),
            'P': pg.transform.smoothscale(pg.image.load('assets/wp.png'), (square_dim, square_dim)),
            'k': pg.transform.smoothscale(pg.image.load('assets/bk.png'), (square_dim, square_dim)),
            'q': pg.transform.smoothscale(pg.image.load('assets/bq.png'), (square_dim, square_dim)),
            'r': pg.transform.smoothscale(pg.image.load('assets/br.png'), (square_dim, square_dim)),
            'b': pg.transform.smoothscale(pg.image.load('assets/bb.png'), (square_dim, square_dim)),
            'n': pg.transform.smoothscale(pg.image.load('assets/bn.png'), (square_dim, square_dim)),
            'p': pg.transform.smoothscale(pg.image.load('assets/bp.png'), (square_dim, square_dim)),
        }

    def draw_pieces(squares, images, board):
        for square in squares:
            if board.board[square]:
                tp = board.board[square].piece_type
                WIN.blit(images[tp.upper() if board.board[square].is_white else tp], squares[square])

    WIDTH, HEIGHT = 520, 520
    WIN = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    pg.display.set_caption('Chess')
    FPS = 30

    colours = {
        'BLACK': (0, 0, 0),
        'LIGHT': (240, 217, 181),
        'DARK': (181, 136, 99),
    }

    game = Game()
    game.board.init()

    run = True
    clock = pg.time.Clock()
    square_selected = None
    while run:
        clock.tick(FPS)

        WIN.fill(colours['BLACK'])

        squares = def_squares()
        draw_squares(squares)
        images = def_images()
        draw_pieces(squares, images, game.board)

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

                    if square_selected is None:
                        square_selected = square_clicked
                    else:
                        game.move_input(square_selected, square_clicked)
                        square_selected = None
                    
                case pg.MOUSEBUTTONUP:
                    square_clicked = None
                    pos = pg.mouse.get_pos()
                    for square, rect in squares.items():
                        if rect.collidepoint(pos):
                            square_clicked = square
                            break
                    
                    if square_clicked is None or square_clicked == square_selected:
                        continue

                    if square_selected is not None:
                        game.move_input(square_selected, square_clicked)
                        square_selected = None

        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    # main_text()
    main()


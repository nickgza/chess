from game import Game

def main_text():
    game = Game()
    game.run_game()
    game.print_score()

def main():
    import pygame as pg

    # setup()
    WIDTH, HEIGHT = 520, 520
    WIN = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    pg.display.set_caption('Chess')
    FPS = 30

    colours = {
        'BLACK': (0, 0, 0),
        'LIGHT': (240, 217, 181),
        'DARK': (181, 136, 99),
    }

    def calculate_top_left(width, height):
        if width > height:
            return ((width - height) // 2, 0)
        else:
            return (0, (height - width) // 2)

    def draw():
        WIN.fill(colours['BLACK'])

        size = pg.display.get_surface().get_size()
        dim = min(size)
        square_dim = round(dim / 8)
        top_left_x, top_left_y = calculate_top_left(*size)

        squares = {
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

        for key, val in squares.items():
            pg.draw.rect(WIN, colours['DARK' if (ord(key[0]) + ord(key[1])) % 2 == 0 else 'LIGHT'], val)

        # images = {
        #     'WHITEKING': pg.transform.scale(pg.image.load('assets/white_king.png').convert_alpha(), (square_dim, square_dim))
        # }

        # WIN.blit(images['WHITEKING'], squares['e1'])
        pg.display.update()

    run = True
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        draw()

    pg.quit()


if __name__ == '__main__':
    # main_text()
    main()


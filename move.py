
class Move:
    start: str
    end: str
    promote_to: str
    captured_type: str
    en_passant: str
    affected_white_king_side_castle: bool
    affected_white_queen_side_castle: bool
    affected_black_king_side_castle: bool
    affected_black_queen_side_castle: bool

    def __init__(self, start, end, promote_to=' '):
        self.start = start
        self.end = end
        self.promote_to = promote_to
    
    def start_file(self):
        return self.start[0]
    
    def start_rank(self):
        return self.start[1]

    def end_file(self):
        return self.end[0]
    
    def end_rank(self):
        return self.end[1]

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    
    def __str__(self):
        return f'{self.start} {self.end}'

    def __repr__(self):
        return str(self)

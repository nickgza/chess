import unittest
import sys
import io
import os
import main
import contextlib

class TestMain(unittest.TestCase):
    def perft(self, file):
        with open(f'tests/{file}.in') as perftin:
            sys.stdin = perftin
            with open(os.devnull, 'w', encoding='utf8') as null:
                with contextlib.redirect_stdout(null):
                    with contextlib.redirect_stderr(io.StringIO()) as out:
                        main.main_text()

        sys.stdin = sys.__stdin__
        with open(f'tests/{file}.out') as perftout:
            self.assertEqual(out.getvalue(), perftout.read())

    def test_perft1(self):
        self.perft('perft1')

    def test_perft2(self):
        self.perft('perft2')

    def test_perft3(self):
        self.perft('perft3')

    def test_perft4(self):
        self.perft('perft4')

    def test_perft5(self):
        self.perft('perft5')

    def test_perft6(self):
        self.perft('perft6')

if __name__ == '__main__':
    unittest.main()

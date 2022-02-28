import unittest
import sys
import io
import os
import main

class TestMain(unittest.TestCase):
    # TODO: setup decorator
    def test_perft1(self):
        with open('tests/perft1.in') as perft1in:
            sys.stdin = perft1in
            with open(os.devnull, 'w', encoding='utf-8') as null:
                sys.stdout = null
                out = io.StringIO()
                sys.stderr = out

                main.main()

                sys.stdin = sys.__stdin__
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
                with open('tests/perft1.out') as perft1out:
                    self.assertEqual(out.getvalue(), perft1out.read())

if __name__ == '__main__':
    unittest.main()

import nqueens
import unittest

class TestTest(unittest.TestCase):
    def test1(self): self.assertEqual(1,1)

class TestShareDiag(unittest.TestCase):
    def test1(self): self.assertEqual(nqueens.share_diag(5,2,2,0), False)
    def test2(self): self.assertEqual(nqueens.share_diag(5,2,4,1), True)
    def test3(self): self.assertEqual(nqueens.share_diag(5,2,4,3), True)

class TestIsColValid(unittest.TestCase):
    def test1(self): self.assertEqual(nqueens.is_col_valid([6,4,2,0,5], 4), True)
    def test2(self): self.assertEqual(nqueens.is_col_valid([2,0,1], 2), False) #Violation b/w 1 & 0
    def test3(self): self.assertEqual(nqueens.is_col_valid([6,4,2,0,5,7,1,3], 7), True)
    def test4(self): self.assertEqual(nqueens.is_col_valid([0,1], 1), False) #Violation b/w 1 & 0
    def test5(self): self.assertEqual(nqueens.is_col_valid([5,6], 1), False) #Violation b/w 5 & 6
    def test6(self): self.assertEqual(nqueens.is_col_valid([0,6,4,3], 3), False) #Violation b/w 4 & 3
    def test7(self): self.assertEqual(nqueens.is_col_valid([0,6,4,5], 3), False) #Violation b/w 4 & 5
    def test8(self): self.assertEqual(nqueens.is_col_valid([5,0,7], 2), False) #Violation b/w 5 & 7

class TestIsBoardValid(unittest.TestCase):
    def test1(self): self.assertEqual(nqueens.is_board_valid([6,4,2,0,5,7,1,3]), True)
    def test2(self): self.assertEqual(nqueens.is_board_valid([4,6,2,0,5,7,1,3]), False) # Clash b/w 4&3
    def test3(self): self.assertEqual(nqueens.is_board_valid([2,0,3,1]), True) 
    def test4(self): self.assertEqual(nqueens.is_board_valid([0,1,2,3]), False) # All clash

if __name__ == "__main__":

    #Run test suite
    unittest.main()    

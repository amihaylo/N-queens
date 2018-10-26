import nqueens
import unittest

class TestTest(unittest.TestCase):
    def test1(self): self.assertEqual(1,1)

class TestShareDiag(unittest.TestCase):
    def test1(self): self.assertEqual(nqueens.share_diag(5,2,2,0), False)
    def test2(self): self.assertEqual(nqueens.share_diag(5,2,4,1), True)
    def test3(self): self.assertEqual(nqueens.share_diag(5,2,4,3), True)

class TestNextRowClashes(unittest.TestCase):
    def test1(self): self.assertEqual(nqueens.next_row_clashes([6,4,2,0,5], 1), True) #Clash with 0
    def test2(self): self.assertEqual(nqueens.next_row_clashes([6,4,2,0,5], 2), True) #Clash with 0
    def test3(self): self.assertEqual(nqueens.next_row_clashes([6,4,2,0,5], 3), False)
    def test4(self): self.assertEqual(nqueens.next_row_clashes([6,4,2,0,5], 4), True) #Clash with 5
    def test5(self): self.assertEqual(nqueens.next_row_clashes([6,4,2,0,5], 6), True) #Clash with 5    
    def test6(self): self.assertEqual(nqueens.next_row_clashes([6,4,2,0,5], 7), False) 
    

class TestIsBoardValid(unittest.TestCase):
    def test1(self): self.assertEqual(nqueens.is_board_valid([6,4,2,0,5,7,1,3]), True)
    def test2(self): self.assertEqual(nqueens.is_board_valid([4,6,2,0,5,7,1,3]), False) # Clash b/w 4&3
    def test3(self): self.assertEqual(nqueens.is_board_valid([2,0,3,1]), True) 
    def test4(self): self.assertEqual(nqueens.is_board_valid([0,1,2,3]), False) # All clash

if __name__ == "__main__":

    #Run test suite
    unittest.main()    

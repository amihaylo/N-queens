import unittest
from board import Board

class TestTest(unittest.TestCase):
    def test1(self): self.assertEqual(1,1)

class TestShareDiag(unittest.TestCase):
    def test1(self): self.assertEqual(Board([]).share_diag(5,2,2,0), False)
    def test2(self): self.assertEqual(Board([]).share_diag(5,2,4,1), True)
    def test3(self): self.assertEqual(Board([]).share_diag(5,2,4,3), True)

class TestIsColValid(unittest.TestCase):
    def test1(self): self.assertEqual(Board([6,4,2,0,5]).is_col_valid(4), True)
    def test2(self): self.assertEqual(Board([2,0,1]).is_col_valid(2), False) #Violation b/w 1 & 0
    def test3(self): self.assertEqual(Board([6,4,2,0,5,7,1,3]).is_col_valid(7), True)
    def test4(self): self.assertEqual(Board([0,1]).is_col_valid(1), False) #Violation b/w 1 & 0
    def test5(self): self.assertEqual(Board([5,6]).is_col_valid(1), False) #Violation b/w 5 & 6
    def test6(self): self.assertEqual(Board([0,6,4,3]).is_col_valid(3), False) #Violation b/w 4 & 3
    def test7(self): self.assertEqual(Board([0,6,4,5]).is_col_valid(3), False) #Violation b/w 4 & 5
    def test8(self): self.assertEqual(Board([5,0,7]).is_col_valid(2), False) #Violation b/w 5 & 7

class TestIsBoardValid(unittest.TestCase):
     def test1(self): self.assertEqual(Board([6,4,2,0,5,7,1,3]).is_valid(), True)
     def test2(self): self.assertEqual(Board([4,6,2,0,5,7,1,3]).is_valid(), False) # Clash b/w 4&3
     def test3(self): self.assertEqual(Board([2,0,3,1]).is_valid(), True) 
     def test4(self): self.assertEqual(Board([0,1,2,3]).is_valid(), False) # All clash

class TestMapRowToCol(unittest.TestCase):
     def test1(self): self.assertEqual(Board([]).row_to_col_representation(),[])
     def test2(self): self.assertEqual(Board([2,0,3,1]).row_to_col_representation(),[1,3,0,2])
     def test3(self): self.assertEqual(Board([6,4,2,0,5,7,1,3]).row_to_col_representation(),[3,6,2,7,1,4,0,5])

if __name__ == "__main__":

    #Run test suite
    unittest.main()    

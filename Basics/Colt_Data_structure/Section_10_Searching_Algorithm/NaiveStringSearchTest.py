import unittest
from NaiveStringSearch import naiveStringSearch

class BinaryTest(unittest.TestCase):

    def test_naiveStringSearch(self):
        self.assertEqual(naiveStringSearch('omlomgomlomgomlomg','omg'), 3)
        self.assertEqual(naiveStringSearch('hello hello hella world','hello'),2)
        self.assertEqual(naiveStringSearch('Hi you there How are you','you'),2)
        self.assertEqual(naiveStringSearch('','hello'),0)
        self.assertEqual(naiveStringSearch("lorie loled", "lol"),1)



if __name__ == "__main__":
    unittest.main()
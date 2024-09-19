import unittest
from app import sumar



class  TestFunctions(unittest.TestCase):
    def test_sumar_function(self):
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(1, 3), 4)




if __name__ == '__main__':
    unittest.main()
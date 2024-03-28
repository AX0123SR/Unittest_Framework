import unittest

class Apptesting(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
         print("Runs before the class starts !! ")


     def setUp(self):
         print("This class method runs before every test method.............")

     @classmethod
     def tearDown(self):
         print("This class method runs after every test method............")

     def test_1(self):
         print("First test case")

     def test_2(self):
         print("Second test case")

     def test_3(self):
         print("Third test case")

     def test_4(self):
         print("Fourth test case")

     @classmethod
     def tearDownClass(cls):
         print("Runs after the class ends !! ")

if __name__ == "__main__":
    unittest.main()
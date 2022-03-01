import unittest

class Apptesting(unittest.TestCase):
     @unittest.SkipTest
     def test_1(self):
         print("First test case")

     @unittest.skip("Skipping this method")
     def test_2(self):
         print("Second test case")

     @unittest.skipIf(2==2, "Condition is True")
     def test_3(self):
         print("Third test case")

     def test_4(self):
         print("Fourth test case")



if __name__ == "__main__":
    unittest.main()
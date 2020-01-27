import unittest
import MyClass

class TestStringMethods(unittest.TestCase):

    def test_addTogether(self):
        self.assertEqual(MyClass.addNumbers(45,17),62)
        

    def test_subTogether(self):
        self.assertEqual(MyClass.subNumbers(62,17),45)


if __name__ == '__main__':
    unittest.main()

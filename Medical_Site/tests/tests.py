import unittest

# Класс для хранения тестов
class MyTests(unittest.TestCase):

    def test_addition(self):
        """Тест на проверку правильности сложения"""
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        """Тест на проверку правильности вычитания"""
        self.assertEqual(5 - 3, 2)

    def test_failure(self):
      """Тест, который должен провалиться"""
      self.assertNotEqual(1,1) # Этот тест провалится


if __name__ == '__main__':
    unittest.main()
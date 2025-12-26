import unittest
import sys
import os

# Добавляем путь к директории с модулями
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'rk1'))

# Импортируем функции из requests
from requests import create_one_to_many, request_1, request_2

class TestOrchestraSystem(unittest.TestCase):

    def test_1(self):
        data = create_one_to_many()
        assert len(data) > 0
        print("Test 1 OK")

    def test_2(self):
        test_data = [('Z', 1, 'C'), ('A', 2, 'B')]
        result = request_1(test_data)
        assert result[0][2] == 'B'
        print("Test 2 OK")

    def test_3(self):
        test_data = [('A', 10, 'X'), ('B', 20, 'X')]
        result = request_2(test_data)
        result_dict = dict(result)
        assert result_dict.get('X') == 30
        print("Test 3 OK")

if __name__ == '__main__':
    unittest.main()

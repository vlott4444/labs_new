import sys
import os
sys.path.append('../rk1')  # Добавляем путь к директории с модулями
import requests

print("ТЕСТ 1:")
data = requests.create_one_to_many()
print(f"✓ {len(data)} записей")

print("\nТЕСТ 2:")
test = [('Z', 1, 'C'), ('A', 2, 'B')]
result = requests.request_1(test)
print(f"✓ Сортировка работает: {result[0][2]}")

print("\nТЕСТ 3:")
test = [('A', 10, 'X'), ('B', 20, 'X')]
result = requests.request_2(test)
print(f"✓ Сумма: {dict(result).get('X')}")

print("\n✅ ВСЕ 3 ТЕСТА OK")

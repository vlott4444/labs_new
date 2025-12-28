import sys
import os

# Добавляем родительскую директорию в путь для импортов
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import requests
import data


class TestRequests:
    """Тесты для запросов из requests.py"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.one_to_many = requests.create_one_to_many()
        self.many_to_many = requests.create_many_to_many()

    def test_create_one_to_many(self):
        """Тест создания связи один-ко-многим"""
        result = requests.create_one_to_many()

        # Проверяем что результат не пустой
        assert len(result) > 0

        # Проверяем структуру данных
        for item in result:
            assert len(item) == 3  # (имя дирижера, стаж, имя оркестра)
            assert isinstance(item[0], str)  # имя дирижера
            assert isinstance(item[1], int)  # стаж
            assert isinstance(item[2], str)  # имя оркестра

        # Проверяем что все дирижеры привязаны к оркестрам
        conductors_in_result = [item[0] for item in result]
        assert 'Светланов' in conductors_in_result
        assert 'Плетнев' in conductors_in_result

    def test_request_1_sorted_by_orchestra(self):
        """Тест запроса 1: сортировка по оркестрам"""
        result = requests.request_1(self.one_to_many)

        # Проверяем что результат отсортирован по названию оркестра
        orchestra_names = [item[2] for item in result]

        # Проверяем что оркестры идут в алфавитном порядке
        assert orchestra_names == sorted(orchestra_names)

        # Проверяем конкретные данные
        first_item = result[0]
        assert isinstance(first_item[0], str)  # имя дирижера
        assert isinstance(first_item[1], int)  # стаж
        assert isinstance(first_item[2], str)  # имя оркестра

    def test_request_2_sum_experience(self):
        """Тест запроса 2: суммарный стаж по оркестрам"""
        result = requests.request_2(self.one_to_many)

        # Проверяем структуру результата
        assert len(result) > 0

        # Проверяем что это список кортежей (имя оркестра, суммарный стаж)
        for orchestra_name, total_exp in result:
            assert isinstance(orchestra_name, str)
            assert isinstance(total_exp, int)
            assert total_exp > 0  # стаж должен быть положительным

        # Проверяем что результат отсортирован по убыванию стажа
        experiences = [exp for _, exp in result]
        assert experiences == sorted(experiences, reverse=True)

        # Проверяем корректность подсчета
        # Для оркестра с id=1 (Большой симфонический) есть 2 дирижера: Светланов(40) и Китаенко(42)
        orchestra_exp_dict = dict(result)
        assert orchestra_exp_dict.get('Большой симфонический оркестр') == 82  # 40 + 42

    def test_request_3_filter_orchestra_keyword(self):
        """Тест запроса 3: фильтрация по слову 'оркестр'"""
        result = requests.request_3(self.many_to_many)

        # Проверяем что это словарь
        assert isinstance(result, dict)

        # Проверяем что ключи содержат слово "оркестр"
        for orchestra_name in result.keys():
            assert 'оркестр' in orchestra_name.lower()

        # Проверяем что для каждого оркестра есть список дирижеров
        for orchestra_name, conductors in result.items():
            assert isinstance(conductors, list)
            assert len(conductors) > 0
            for conductor in conductors:
                assert isinstance(conductor, str)

        # Проверяем конкретный оркестр
        assert 'Большой симфонический оркестр' in result
        assert 'Светланов' in result['Большой симфонический оркестр']

    def test_request_1_with_empty_data(self):
        """Тест запроса 1 с пустыми данными"""
        empty_one_to_many = []
        result = requests.request_1(empty_one_to_many)
        assert result == []

    def test_request_2_with_single_conductor(self):
        """Тест запроса 2 с одним дирижером"""
        test_data = [('Дирижер1', 10, 'Оркестр1')]
        result = requests.request_2(test_data)

        assert len(result) == 1
        assert result[0][0] == 'Оркестр1'
        assert result[0][1] == 10

    def test_main_function_runs_without_errors(self):
        """Тест что основная функция выполняется без ошибок"""
        try:
            requests.main()
            # Если дошли сюда без исключений - тест пройден
            assert True
        except Exception as e:
            assert False, f"main() вызвала исключение: {e}"


def test_data_integrity():
    """Тест целостности данных"""
    # Проверяем что данные загружаются корректно
    assert len(data.orchestras) == 5
    assert len(data.conductors) == 7
    assert len(data.conductors_orchestras) == 12

    # Проверяем типы данных
    for conductor in data.conductors:
        assert hasattr(conductor, 'id')
        assert hasattr(conductor, 'name')
        assert hasattr(conductor, 'experience')
        assert hasattr(conductor, 'orchestra_id')
        assert isinstance(conductor.experience, int)

    for orchestra in data.orchestras:
        assert hasattr(orchestra, 'id')
        assert hasattr(orchestra, 'name')


if __name__ == "__main__":
    print("Запуск тестов...")

    # Создаем экземпляр тестового класса
    test_instance = TestRequests()

    # Запускаем setup
    test_instance.setup_method()

    # Запускаем тесты по одному
    tests = [
        ("test_create_one_to_many", test_instance.test_create_one_to_many),
        ("test_request_1_sorted_by_orchestra", test_instance.test_request_1_sorted_by_orchestra),
        ("test_request_2_sum_experience", test_instance.test_request_2_sum_experience),
        ("test_request_3_filter_orchestra_keyword", test_instance.test_request_3_filter_orchestra_keyword),
        ("test_data_integrity", test_data_integrity),
        ("test_main_function_runs_without_errors", test_instance.test_main_function_runs_without_errors),
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        try:
            if test_name.startswith("test_"):
                # Это метод класса
                test_func()
            else:
                # Это обычная функция
                test_func()
            print(f"✅ {test_name}: PASSED")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name}: FAILED - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {type(e).__name__}: {e}")
            failed += 1

    print(f"\nИтого: {passed} пройдено, {failed} упало")

    if failed == 0:
        print("🎉 Все тесты прошли успешно!")
        sys.exit(0)
    else:
        print("💥 Некоторые тесты не прошли")
        sys.exit(1)
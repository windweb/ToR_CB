import os
import pandas as pd
import pytest

# Функция для загрузки CSV файла с использованием указанного разделителя
def load_csv(file_path):
    return pd.read_csv(file_path, delimiter=';', encoding='ISO-8859-1')

# Ожидаемые столбцы в файле CSV
EXPECTED_COLUMNS = [
    "PayerBIC", "PayeeBIC", "Sum", "EDNo", "EDDate", "Purpose"
]

# Тест: проверка наличия всех ожидаемых столбцов
def test_csv_columns_present():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'ED101.csv')
    ed101_data = load_csv(file_path)

    # Проверка, что все ожидаемые столбцы присутствуют
    assert all(column in ed101_data.columns for column in EXPECTED_COLUMNS), \
        "Один или несколько ожидаемых столбцов отсутствуют в файле CSV."

# Тест: проверка правильности разделителя
def test_csv_delimiter():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'ED101.csv')
    ed101_data = load_csv(file_path)

    # Проверка, что данные разделены корректно
    assert len(ed101_data.columns) > 1, "В файле CSV неправильно используется разделитель ';'."

# Запуск тестов через pytest
if __name__ == "__main__":
    pytest.main()

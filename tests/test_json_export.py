import os
import json
import pytest


def test_json_file_exists():
    """Проверка существования файла ED101.json в корневом каталоге."""
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'ED101.json')
    assert os.path.exists(file_path), "Файл ED101.json не найден в корневом каталоге."


# def test_json_structure():
#     """Проверка структуры файла ED101.json."""
#     root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#     file_path = os.path.join(root_dir, 'ED101.json')
#
#     with open(file_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#
#     # Проверка ключей заголовка
#     required_keys = ['SystemCode', 'Sum', 'EDQuantity', 'EDNo', 'EDDate', 'EDAuthor', 'ED101']
#     for key in required_keys:
#         assert key in data, f"Отсутствует ключ {key} в заголовке файла ED101.json"
#
#     # Проверка структуры документов в ED101
#     assert isinstance(data['ED101'], list), "ED101 должен быть массивом"
#     for doc in data['ED101']:
#         assert 'Sum' in doc, "Отсутствует реквизит 'Sum' в документе ED101"
#         assert 'EDNo' in doc, "Отсутствует реквизит 'EDNo' в документе ED101"
#         assert 'PayerName' in doc, "Отсутствует реквизит 'PayerName' в документе ED101"
#         assert 'PayeeName' in doc, "Отсутствует реквизит 'PayeeName' в документе ED101"

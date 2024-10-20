import os
import xml.etree.ElementTree as ET
import pytest

# Загрузка XML файла
def load_xml(file_path):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = ET.parse(file_path)
    return tree

# 3.4. Проверка общей суммы и количества документов ED101
def test_summary_information():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = load_xml(file_path)
    root = tree.getroot()

    total_sum = 0
    total_documents = 0

    for ed101 in root.findall('ED101'):
        sum_element = ed101.find('Sum')
        if sum_element is not None:
            total_sum += int(sum_element.text)
        total_documents += 1

    # Проверка, что общая сумма и количество документов корректно посчитаны
    assert total_documents > 0, "Количество документов ED101 должно быть больше 0."
    assert total_sum > 0, "Общая сумма по документам ED101 должна быть больше 0."

# Запуск тестов через pytest
if __name__ == "__main__":
    pytest.main()

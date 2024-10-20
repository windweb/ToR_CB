import os
import xml.etree.ElementTree as ET
import pytest

# Загрузка XML файла
def load_xml(file_path):
    tree = ET.parse(file_path)
    return tree

# 3.2. Проверка корректности импорта данных из файла PacketEPD.xml
def test_import_epd_data():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = load_xml(file_path)
    root = tree.getroot()

    ed101_elements = root.findall('ED101')
    assert len(ed101_elements) > 0, "Документы ED101 не найдены в файле PacketEPD.xml."

# Запуск тестов через pytest
if __name__ == "__main__":
    pytest.main()

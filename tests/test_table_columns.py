import os
import xml.etree.ElementTree as ET
import pytest

# Загрузка XML файла
def load_xml(file_path):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = ET.parse(file_path)
    return tree

# 3.3. Проверка корректности столбцов таблицы для ED101
def test_table_columns():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = load_xml(file_path)
    root = tree.getroot()

    for ed101 in root.findall('ED101'):
        payer_bic = ed101.find('./Payer/Bank').get('BIC')
        payee_bic = ed101.find('./Payee/Bank').get('BIC')
        ed_no = ed101.get('EDNo')
        ed_date = ed101.get('EDDate')
        purpose = ed101.find('Purpose')
        sum_element = ed101.find('Sum')

        # Проверяем, что необходимые поля существуют
        assert payer_bic is not None, "Отсутствует БИК Плательщика"
        assert payee_bic is not None, "Отсутствует БИК Получателя"
        assert ed_no is not None, "Отсутствует номер документа"
        assert ed_date is not None, "Отсутствует дата документа"
        assert purpose is not None, "Отсутствует назначение платежа"
        assert sum_element is not None, "Отсутствует сумма"

# Запуск тестов через pytest
if __name__ == "__main__":
    pytest.main()

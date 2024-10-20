import os
import xml.etree.ElementTree as ET
import pytest


# Загрузка XML файла
def load_xml(file_path):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = ET.parse(file_path)
    return tree


# Проверка обязательных реквизитов заголовка
def test_header_requisites():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    tree = load_xml(file_path)
    root = tree.getroot()

    # Проверка наличия обязательных атрибутов в заголовке PacketEPD
    assert 'EDNo' in root.attrib, "Отсутствует атрибут EDNo в заголовке"
    assert 'EDDate' in root.attrib, "Отсутствует атрибут EDDate в заголовке"
    assert 'EDAuthor' in root.attrib, "Отсутствует атрибут EDAuthor в заголовке"
    assert 'EDQuantity' in root.attrib, "Отсутствует атрибут EDQuantity в заголовке"
    assert 'Sum' in root.attrib, "Отсутствует атрибут Sum в заголовке"
    assert 'SystemCode' in root.attrib, "Отсутствует атрибут SystemCode в заголовке"


# Проверка обязательных реквизитов ED101
def test_ed101_requisites():
    tree = load_xml('../PacketEPD.xml')
    root = tree.getroot()

    for ed101 in root.findall('ED101'):
        # Проверка обязательных реквизитов ED101
        assert ed101.find('AccDoc') is not None, "Отсутствует элемент AccDoc"
        assert ed101.find('Payer') is not None, "Отсутствует элемент Payer"
        assert ed101.find('Payee') is not None, "Отсутствует элемент Payee"
        assert ed101.find('Purpose') is not None, "Отсутствует элемент Purpose"

        # Проверка реквизитов Payer
        payer = ed101.find('Payer')
        assert payer.find('Name') is not None, "Отсутствует имя плательщика"
        assert payer.find('Bank') is not None, "Отсутствует банк плательщика"
        assert payer.find('Bank').get('BIC') is not None, "Отсутствует BIC плательщика"
        assert payer.find('Bank').get('CorrespAcc') is not None, "Отсутствует корреспондентский счет плательщика"

        # Проверка реквизитов Payee
        payee = ed101.find('Payee')
        assert payee.find('Name') is not None, "Отсутствует имя получателя"
        assert payee.find('Bank') is not None, "Отсутствует банк получателя"
        assert payee.find('Bank').get('BIC') is not None, "Отсутствует BIC получателя"
        assert payee.find('Bank').get('CorrespAcc') is not None, "Отсутствует корреспондентский счет получателя"


# Запуск тестов через pytest, если файл запускается напрямую
if __name__ == "__main__":
    pytest.main()

import os
import pytest

# 3.1. Проверка наличия файла PacketEPD.xml в каталоге
def test_file_existence():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(root_dir, 'PacketEPD.xml')
    assert os.path.exists(file_path), f"Файл {file_path} не найден в каталоге приложения."

# Запуск тестов через pytest
if __name__ == "__main__":
    pytest.main()

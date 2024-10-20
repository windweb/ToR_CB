# headHunterTest
Содержит тестовое приложение для соискателей
Запуск проверен на Win 7 64X

Структура проекта


## [README.md](README.md) 

    
## [Анализ требований](requirements_analysis.md)

## [Тестовый план](t_plan.md)

## [Тест-кейсы](t_cases)
### Тест-кейсы для функционального тестирования приложения [testqawin.exe](testqawin.exe)


## Автоматизация
### Требования
 - Для работы проекта требуется установленный Python версии 3.8 или выше.
 - Установка зависимостей `pip install -r requirements.txt`
 - Запуск тестов `pytest`


## [Баг-репорты](bug_reports)

- [функциональность активации приложения](bug_reports%2Fbr0001_application_activation.md)
- [функциональность «Convert -> ED807toPacketEPD](bug_reports%2Fbr0002_converting_an_ED807_to_PacketEPD.md)
- [функциональность «Импорт -> PacketEPD»](bug_reports%2Fbr0003_import_PacketEPD_with_missing_sum.md)
- [функциональность «Import -> PacketEPD](bug_reports%2Fbr0004_import_PacketEPD_interface_problem.md)
- [функциональность «Export -> to JSON»](bug_reports%2Fbr0005_export_to_JSON_invalid_filename.md)

### Файлы 

- [20241020_ED807_full.xml](docs%2F20241020ED01OSBR%2F20241020_ED807_full.xml)
- [PacketEPD.xml](PacketEPD.xml)
- [ED101.csv](ED101.csv)
- [PacketEPD.json](PacketEPD.json)
- [log.txt](log.txt)

# Баг-репорт N 0002

- **Проект**: TestQAWin
- **Название документа**: Баг-репорт на функциональность «Convert -> ED807toPacketEPD»
- **Ссылка на требования**: Техническое задание, пункт 2 (Конвертация ED807 в PacketEPD)
- **Цель проверки**: Проверить корректность работы функциональности конвертации файла ED807 в PacketEPD
- **Дата проведения**: 20.10.2024
- **Исполнитель**: Kirill Aydarov
- **Среда тестирования**: Windows 7 64-bit, приложение testqawin.exe
- **Шаги теста**:
   1. Открыть меню «? -> О программе».
   2. Ввести корректный ключ активации (AYDAROVKIRILL@YANDEX.RU).
   3. Нажать кнопку «Ок».
   4. Открыть меню «Convert -> ED807toPacketEPD».
   5. Выбрать правильный файл [20241020_ED807_full.xml](..%2Fvalid%20ED807%2F20241020_ED807_full.xml) или из архива 20241020ED01OSBR.zip http://cbr.ru/Queries/XsltBlock/File/101478?fileId=0 .
   6. Убедиться, что файл PacketEPD.xml создан успешно.
   7. Переименовать другой файл (например, [ED807.xml](..%2Finvalid%20ED807%2FED807.xml) из архива http://cbr.ru/Content/Document/File/92276/EDExamples.zip) в ED807.xml и повторить конвертацию.
   8. Проверить результаты.
- **Ожидаемый результат**:
   1. При выборе корректного файла [20241020_ED807_full.xml](..%2Fvalid%20ED807%2F20241020_ED807_full.xml) — успешная конвертация и создание PacketEPD.xml.
   2. При выборе некорректного файла (например,[ED807.xml](..%2Finvalid%20ED807%2FED807.xml) , который не соответствует структуре ED807) — сообщение об ошибке, конвертация не должна завершаться успешно.
   3. Также при создании нового файла [PacketEPD.xml](..%2FPacketEPD.xml) необходимо уведомление о перезаписи файла, либо создание уникального файла с другим именем.
- **Фактический результат**:
   1. Файл PacketEPD.xml был создан успешно для корректного файла ED807.xml.
   2. При выборе некорректного файла (ED408.xml, переименованного в ED807.xml) также появилось сообщение о том, что конвертация прошла успешно, и файл PacketEPD.xml был перезаписан без проверки структуры файла.
- **Статус бага**: Открыт
- **Серьезность бага**: Высокая (Отсутствие валидации структуры данных может привести к созданию некорректных данных)
- **Приоритет устранения**: Высокий (Необходимо для корректного использования программы)
- **Прикрепленный файл**: 
  - корректный ED807.xml: [20241020_ED807_full.xml](..%2Fvalid%20ED807%2F20241020_ED807_full.xml)
  - некорректный ED408.xml: [ED807.xml](..%2Finvalid%20ED807%2FED807.xml)
- **Комментарии**:
  - Этот баг касается двух аспектов:
  1. Отсутствие валидации файла перед конвертацией (некорректный файл также конвертируется).
  2. Перезапись существующего файла PacketEPD.xml без уведомления или создания уникального имени файла.
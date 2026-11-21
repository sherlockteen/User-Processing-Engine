# User-Processing-Engine

![screenshot_working.png](assets/screenshot_working.png)

Консольная программа для обработки пользовательских данных из CSV и JSON с использованием конфигурационного файла INI.

Программа объединяет данные пользователей и электронные адреса, проверяет записи по заданным правилам, разделяет их на принятые и отклонённые, а затем экспортирует результат в CSV.

## Возможности
* Загрузка пользователей из CSV.
* Загрузка email-адресов из JSON.
* Чтение параметров обработки из INI.
* Объединение данных пользователей по id.
* Проверка возраста и наличия email.
* Обработка некорректных значений возраста.
* Сохранение нескольких причин отклонения записи.
* Экспорт успешно обработанных пользователей в CSV.
* Вывод итоговой статистики.


# Запуск
Требуется Python 3.8 или новее.

Сторонние библиотеки не требуются

```bash
git clone https://github.com/sherlockteen/User-Processing-Engine.git
cd User-Processing-Engine
python3 main.py
```
Перед запуском разместите входные файлы в директории data/ и настройте config/config.ini.

# Разработано с ❤️ by sherlockteen.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)]()
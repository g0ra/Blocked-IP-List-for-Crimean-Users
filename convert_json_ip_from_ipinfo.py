"""
Преобразует получаемые IP адреса из JSON формата в текст для определенной AS

Порядок действий:
1. Зайти на сайт https://ipinfo.io под своей учетной записью
2. Произвести поиск по определенной AS
3. Полученный JSON вывод скопировать в JSON файл
4. Прописать в переменной file_path путь к сохраненному файлу
5. Запустить скрипт
6. Вывод скопировать на новую вкладку в ASKozlov.xls
"""
import json

file_path = r"d:\temp\delete\asn16509.json"
f = open(r"d:\temp\delete\asn16509.json", "r")
data = json.loads(f.read())
for i in data['prefixes']:
    print(i['netblock'])
# INT - 1
Функциональное и первоманс-тестирование запроса `SELECT str LIKE pattern` в PostgreSQL
## Установка
 1. Установить python3 и docker
    
 2. Настроить виртуальное окружение
    ```
    python3 -m venv /path/to/venv
    source /path/to/venv/activate
    ```
 3. Поставить пакеты:
    ```
    pip install -r requirements.txt
    ```
 4. Запустить:
    ```
    pytest
    ```
## Описание
База данных создается и тестируется в Docker-контейнере с помощью библиотеки [testcontainers](https://testcontainers-python.readthedocs.io/en/latest/).
Тестовые данные генерируются с использованием библиотеки [Faker](https://faker.readthedocs.io/en/master/). Каждый тест происходит на новых данных.

## Результаты тестирования
 1. Данные: `Имя Фамилия`
    Паттерн: `A%`
 
   ![image](https://github.com/Alex-Namat/INT-1/assets/24422451/4c69f655-fecb-4422-bc9a-4abf4978e9b9)
   
 2. Данные: `Имя Фамилия`
    Паттерн: `%Flo%`
 
   ![image](https://github.com/Alex-Namat/INT-1/assets/24422451/571d8a65-76cc-427e-a087-49034e4b2b7d)
   
 3. Данные: `email`
    Паттерн: `%@example.net`
 
   ![image](https://github.com/Alex-Namat/INT-1/assets/24422451/5e2958d7-7fe8-4bd0-a7a8-4acd433864f4)

 4. Данные: `email`
    Паттерн: `%@example.___`
    
   ![image](https://github.com/Alex-Namat/INT-1/assets/24422451/3d817fb4-9fb3-4c8d-b645-b03c34173f53)

 6. Данные: `uri`
    Паттерн: `____s%.html`
    
   ![image](https://github.com/Alex-Namat/INT-1/assets/24422451/ee3b9ad8-944b-4666-bd6b-601fe9d44dcb)

 7. Данные: `uri`
    Паттерн: `https://www.%`

   ![image](https://github.com/Alex-Namat/INT-1/assets/24422451/1c5f55c4-cc51-4596-8e2c-9736c2cb6b29)


## Выводы
Индексы для `SELECT str LIKE pattern` в PostgreSQL имеет смысл применять только на больших данных от 100000 строк, при этом сам паттерн должен быть достаточно длинным. В ином случае запросы с индексом на строку работают стабильно медленнее, нежели чем запросы без использования индексов.

Насколько я понимаю, паттерны типа `%Flo%` и `%@example.net` не используют индексы в MySQL, насчёт Postgresa я такой информации не нашёл. По тестам существенной разницы не обнаружил.





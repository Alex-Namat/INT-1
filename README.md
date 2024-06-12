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
База данных создается и тестируется в Docker-контейнере с помощью библиотеки testcontainers.
Тестовые данные генерируются с использованием библиотеки Faker.

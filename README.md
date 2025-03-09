# Sprint_5
- Проект автоматизации тестирования онлайн-сервиса Stellar Burgers

## Требования
- Для запуска тестов должны быть установлены пакеты pytest и selenium
- Запуск всех тестов выполянется командой pytest -v
- driver - фикстура для создания драйвера Chrome в conftest.py
- auth_driver - фикстура для создания драйвера Chrome с авторизацией в conftest.py
- локаторы в locators.py
- URL главной страницы в config.py 
- generate_name_email_password - генератор имени, email и пароля в helpers.py
- тестовые данные для авторизации в data.py
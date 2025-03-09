from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    REGISTRATION_NAME_FIELD = By.XPATH, ".//label[text()='Имя']//..//input" # ввод имени в форме регистрации
    REGISTRATION_EMAIL_FIELD = By.XPATH, ".//label[text()='Email']//..//input"  # ввод email в форме регистрации
    REGISTRATION_PASSWORD_FIELD = By.NAME, "Пароль" # ввод пароля в форме регистрации
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']" # кнопки "Войти" в форме регистрации
    REGISTRATION_MESSAGE_PASSWORD = By.XPATH, ".//form/fieldset[3]//p" # сообщение "Некорректный пароль" в форме регистрации

    AUTH_EMAIL_FIELD = By.XPATH, ".//label[text()='Email']//..//input" # ввод email в форме авторизации
    AUTH_PASSWORD_FIELD = By.NAME, "Пароль" # ввод пароля в форме авторизации
    AUTH_BUTTON = By.XPATH, ".//button[text()='Войти']" # кнопка "Войти" в форме авторизации

    BUTTON_LOGIN_TO_ACCOUNT = By.XPATH, ".//button[text()='Войти в аккаунт']" # кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_PAGE = By.LINK_TEXT, "Личный Кабинет" # кнопка "Личный кабинет" на главной странице
    LINK_LOGIN_FROM_REGISTRATION = By.LINK_TEXT, "Войти" # ссылка "Войти" на странице регистрации
    LINK_LOGIN_FROM_PASSWORD_RECOVERY = By.LINK_TEXT, "Войти" # ссылка "Войти на странице восстановления пароля

    LINK_TO_CONSTRUCTOR = By.LINK_TEXT, "Конструктор" # ссылка на главную страницу кликом на конструктор
    LINK_TO_LOGO = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']" # ссылка на главную страницу кликом на логотип
    BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, "//button[text()='Выход']" # кнопка "Выйти в личном кабинете

    BUTTON_ORDER = By.XPATH, "//button[text()='Оформить заказ']" # кнопка "Оформить заказ" для авторизованного пользователя

    BUTTON_BUNS = By.XPATH, ".//main//..//span[text()='Булки']" # кнопка "Булки" в конструкторе
    BUTTON_SAUCES = By.XPATH, ".//main//..//span[text()='Соусы']" # кнопка "Соусы" в конструкторе
    BUTTON_FILLINGS = By.XPATH, ".//main//..//span[text()='Начинки']" # кнопка "Начинки" в конструкторе

    CURRENT_BUNS = By.XPATH, ".//main//..//div[contains(@class, 'current')]/span[text()='Булки']" # текущий раздел "Булки"
    CURRENT_SAUCES = By.XPATH, ".//main//..//div[contains(@class, 'current')]/span[text()='Соусы']" # текущий раздел "Соусы"
    CURRENT_FILLINGS = By.XPATH, ".//main//..//div[contains(@class, 'current')]/span[text()='Начинки']" # текущий раздел "Начинки"

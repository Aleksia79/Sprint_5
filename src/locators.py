from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    REGISTRATION_NAME_FIELD = By.XPATH, ".//form/fieldset[1]/div/div/input" # ввод имени в форме регистрации
    REGISTRATION_EMAIL_FIELD = By.XPATH, ".//form/fieldset[2]/div/div/input" # ввод email в форме регистрации
    REGISTRATION_PASSWORD_FIELD = By.NAME, "Пароль" # ввод пароля в форме регистрации
    REGISTRATION_BUTTON = By.XPATH, ".//form/button[text()='Зарегистрироваться']" # кнопки "Войти" в форме регистрации
    REGISTRATION_MESSAGE_PASSWORD = By.XPATH, ".//form/fieldset[3]//p" # сообщение "Некорректный пароль" в форме регистрации

    AUTH_EMAIL_FIELD = By.XPATH, ".//form/fieldset[1]/div/div/input" # ввод email в форме авторизации
    AUTH_PASSWORD_FIELD = By.NAME, "Пароль" # ввод пароля в форме авторизации
    AUTH_BUTTON = By.XPATH, ".//main/div/form/button" # кнопка "Войти" в форме авторизации

    BUTTON_LOGIN_TO_ACCOUNT = By.XPATH, ".//section[2]/div/button" # кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_PAGE = By.XPATH, ".//header/nav/a/p" # кнопка "Личный кабинет" на главной странице
    LINK_LOGIN_FROM_REGISTRATION = By.LINK_TEXT, "Войти" # ссылка "Войти" на странице регистрации
    LINK_LOGIN_FROM_PASSWORD_RECOVERY = By.LINK_TEXT, "Войти" # ссылка "Войти на странице восстановления пароля

    LINK_TO_CONSTRUCTOR = By.XPATH, ".//header/nav/ul/li[1]/a/p" # ссылка на главную страницу кликом на конструктор
    LINK_TO_LOGO = By.XPATH, ".//header/nav/div/a" # ссылка на главную страницу кликом на логотип
    BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, ".//main/div/nav/ul/li[3]/button" # кнопка "Выйти в личном кабинете

    BUTTON_ORDER = By.XPATH, ".//main/section[2]/div/button" # кнопка "Оформить заказ" для авторизованного пользователя

    BUTTON_BUNS = By.XPATH, ".//main/section[1]/div[1]/div[1]" # кнопка "Булки" в конструкторе
    BUTTON_SAUCES = By.XPATH, ".//main/section[1]/div[1]/div[2]" # кнопка "Соусы" в конструкторе
    BUTTON_FILLINGS = By.XPATH, ".//main/section[1]/div[1]/div[3]" # кнопка "Начинки" в конструкторе

    CURRENT_BUNS = By.XPATH, ".//main/section[1]/div[1]/div[1][contains(@class, 'current')]" # текущий раздел "Булки"
    CURRENT_SAUCES = By.XPATH, ".//main/section[1]/div[1]/div[2][contains(@class, 'current')]" # текущий раздел "Соусы"
    CURRENT_FILLINGS = By.XPATH, ".//main/section[1]/div[1]/div[3][contains(@class, 'current')]" # текущий раздел "Начинки"

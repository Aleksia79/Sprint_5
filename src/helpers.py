import faker

from random import randint

# генерация имени, email и пароля
def generate_name_email_password():
    fake = faker.Faker()
    name = fake.name()
    email = f'{"".join(chr(randint(97, 122)) for _ in range(7))}{fake.email()}'
    password = fake.password(length = randint(6,10))
    return name, email, password

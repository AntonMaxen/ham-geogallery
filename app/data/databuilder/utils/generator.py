from sqlalchemy.sql.expression import func
from app.data.db import session
import random
import os
import hashlib
import decimal
from app.data.databuilder.utils.image_downloader import download_image
from app.data.databuilder.utils import get_file_binary_data

from faker import Faker
fake = Faker()


def get_random_word():
    return fake.word()


def get_random_words(amount=3, unique=True):
    return fake.words(nb=amount, unique=unique)


def get_random_text(max_chars=200):
    return fake.text(max_nb_chars=max_chars)


def get_random_first_name():
    return fake.first_name()


def get_random_last_name():
    return fake.last_name()


def get_random_email():
    return fake.email()


def get_random_username():
    return fake.simple_profile()['username']


def get_random_hash():
    return fake.sha256()


def get_random_password(length=10):
    return fake.password(length=length)


def get_random_phonenumber():
    return fake.phone_number()


def get_random_date():
    return fake.past_date()


def get_random_number(min_v, max_v):
    return random.randint(min_v, max_v)


def get_random_decimal(tot_numbers, decimals):
    return decimal.Decimal(
        random.randrange(10 ** tot_numbers)
    ) / 10 ** decimals


def get_random_location():
    return fake.location_on_land()


def get_random_image_data():
    filename = download_image('https://picsum.photos/200')
    if filename is not None:
        return get_file_binary_data(filename)


def get_hash_salt(password):
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return {
        "salt": salt.hex(),
        "hash": hash.hex()
    }


if __name__ == '__main__':
    print(get_random_decimal(2, 1))
    print(get_random_words(amount=5, unique=False))
    get_random_image_data()


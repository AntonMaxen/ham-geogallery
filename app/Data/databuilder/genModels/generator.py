from sqlalchemy.sql.expression import func
from app.Data.db import session
import random
import os
import hashlib

from faker import Faker
fake = Faker()


def get_random_word():
    return fake.word()


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


def get_random_number(min, max):
    return random.randint(min, max)


def get_random_location():
    return fake.location_on_land()


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
    pass


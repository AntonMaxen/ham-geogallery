from sqlalchemy.sql.expression import func
from app.Data.db import session

from faker import Faker
fake = Faker()


def get_random_word():
    return fake.word()





if __name__ == '__main__':
    print(get_random_word())

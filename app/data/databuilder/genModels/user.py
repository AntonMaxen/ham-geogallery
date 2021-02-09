import app.data.databuilder.utils.generator as gen
from werkzeug.security import generate_password_hash
import random


class GenUser:
    def __init__(self):
        self.FirstName = gen.get_random_first_name()
        self.LastName = gen.get_random_last_name()
        self.Email = str(random.randint(1, 1000000)) + gen.get_random_email()
        self.Username = gen.get_random_username() + \
            str(random.randint(1, 1000000))
        hash_salt = generate_password_hash(
            gen.get_random_password(),
            method='sha256',
            salt_length=32
        )
        self.Hash = hash_salt
        self.PhoneNumber = gen.get_random_phonenumber()
        self.DateOfBirth = gen.get_random_date()
        self.JoinDate = gen.get_random_date()
        self.PermissionLevel = gen.get_random_number(0, 255)

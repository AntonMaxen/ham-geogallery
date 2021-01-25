import app.data.databuilder.utils.generator as gen
import random


class GenUser:
    def __init__(self):
        self.FirstName = gen.get_random_first_name()
        self.LastName = gen.get_random_last_name()
        self.Email = str(random.randint(1, 1000000)) + gen.get_random_email()
        self.Username = gen.get_random_username() + \
            str(random.randint(1, 1000000))
        hash_salt = gen.get_hash_salt(gen.get_random_password())
        self.Hash = hash_salt['hash']
        self.Salt = hash_salt['salt']
        self.PhoneNumber = gen.get_random_phonenumber()
        self.DateOfBirth = gen.get_random_date()
        self.JoinDate = gen.get_random_date()
        self.PermissionLevel = gen.get_random_number(0, 255)


if __name__ == '__main__':
    user = GenUser()
    print(user.__dict__)

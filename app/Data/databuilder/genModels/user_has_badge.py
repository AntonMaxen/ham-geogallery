from app.Data.models.model_imports import *
import app.Data.databuilder.utils.generator as gen
import app.Data.repository.table_functions as tf


class GenUserBadge:
    def __init__(self):
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_badge = tf.get_random_row(Badge)
        self.BadgeId = getattr(random_badge, 'Id', None)
        self.DateAcquired = gen.get_random_date()


if __name__ == '__main__':
    gen_user_has_badge = GenUserBadge()
    print(gen_user_has_badge.__dict__)

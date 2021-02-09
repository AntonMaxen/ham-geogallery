from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf


class GenUserBadge:
    def __init__(self):
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_badge = tf.get_random_row(Badge)
        self.BadgeId = getattr(random_badge, 'Id', None)
        self.DateAcquired = gen.get_random_date()

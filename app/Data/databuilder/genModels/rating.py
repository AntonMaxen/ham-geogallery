from app.Data.models.model_imports import *
import app.Data.databuilder.utils.generator as gen
import app.Data.repository.table_functions as tf


class GenRating:
    def __init__(self):
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_location = tf.get_random_row(Location)
        self.LocationId = getattr(random_location, 'Id', None)
        self.Score = gen.get_random_decimal(2, 1)


if __name__ == '__main__':
    g_rating = GenRating()
    print(g_rating.__dict__)

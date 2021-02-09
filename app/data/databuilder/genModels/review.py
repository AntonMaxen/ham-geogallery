from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf


class GenReview:
    def __init__(self):
        self.Title = gen.get_random_text(
            max_chars=gen.get_random_number(5, 45)
        ).replace('.', '')
        self.ReviewText = gen.get_random_text(
            max_chars=gen.get_random_number(5, 1024)
        )
        self.Score = gen.get_random_decimal(2, 1)
        self.DateCreated = gen.get_random_date()
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_location = tf.get_random_row(Location)
        self.LocationId = getattr(random_location, 'Id', None)

from app.data.models.model_imports import *
import app.data.repository.table_functions as tf


class GenVisitedLocation:
    def __init__(self):
        random_location = tf.get_random_row(Location)
        self.LocationId = getattr(random_location, 'Id', None)
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)

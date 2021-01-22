from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf
import os


class GenPicture:
    def __init__(self):
        file_path = gen.download_image('https://picsum.photos/200')
        file_name = os.path.split(file_path)[-1]
        image_name = file_name.split('.')[0]
        self.ImageName = image_name
        self.Date = gen.get_random_date()
        most_recent_row = tf.get_highest_row(Picture)
        recent_row_id = getattr(most_recent_row, 'Id', 0)
        self.FileName = file_name
        random_user = tf.get_random_row(User)
        self.UserId = getattr(random_user, 'Id', None)
        random_location = tf.get_random_row(Location)
        self.LocationId = getattr(random_location, 'Id', None)


if __name__ == '__main__':
    gen_picture = GenPicture()
    print(gen_picture.__dict__)

import app.data.repository.picture_repo as pr


def get_pictures_by_location_id(location_id):
    return pr.get_pictures_by_location_id(location_id)


if __name__ == '__main__':
    pass

import app.data.repository.picture_repo as pr


def get_pictures_by_location_id(location_id):
    return pr.get_pictures_by_location_id(location_id)


def get_most_recent_row():
    return pr.get_most_recent_row()


def get_pictures_by_location_ordered_by_id_desc(location_id):
    return pr.get_pictures_by_colname_desc_id(
        location_id,
        col_name='LocationId'
    )


def add_picture(row_dict):
    return pr.add_picture(row_dict)

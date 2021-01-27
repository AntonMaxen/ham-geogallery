import app.data.repository.location_repo as lr


def get_location_by_place_name(place_name):
    return lr.search_location('Place', place_name)


def get_location_by_id(location_id):
    return lr.get_location_by_id(location_id)


def get_all_locations():
    return lr.get_all_locations()


def get_location(place_name):
    return lr.get_locations(place_name)


if __name__ == '__main__':
    pass

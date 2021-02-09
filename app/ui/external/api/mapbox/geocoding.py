import requests
from app.ui.external.api.mapbox import api_key


def get_geoinformation_by_latlng(lat, lng, **kwargs):
    base = 'https://api.mapbox.com/geocoding/v5'
    endpoint = 'mapbox.places'
    url = f'{base}/{endpoint}/{lat},{lng}.json?access_token={api_key}'
    result = requests.get(url)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return {'status': 404}

    return result.json()

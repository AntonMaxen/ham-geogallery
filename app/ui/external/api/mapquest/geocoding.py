from app.ui.external.api.mapquest import api_key_personal, api_key_general
import requests


def get_geoinformation_by_latlng(lat, lng, **kwargs):
    include_road_metadata = kwargs.get(
        'includeRoadMetadata',
        'false')
    include_nearest_intersection = kwargs.get(
        'includeNearestIntersection',
        'false'
    )

    endpoint = 'http://www.mapquestapi.com/geocoding/v1'
    url = f'{endpoint}/reverse?' \
        f'key={api_key_general}&' \
        f'location={lat}%2C{lng}&' \
        f'outFormat=json'

    print(url)
    result = requests.get(url)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return {'status': 404}

    print(result.request)
    if 'application/json' in result.headers.get('Content-Type', ''):
        json_obj = result.json()
        json_obj['status'] = 200
        return json_obj
    else:
        print(result.content)
        return {'status': 404}


if __name__ == '__main__':
    get_geoinformation_by_latlng(30.333472, -81.470448)
    pass

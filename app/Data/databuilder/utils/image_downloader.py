import requests
import shutil
import time
from pathlib import Path
from app.utils import get_project_root
import os


def download_image(image_url, suffix='.png'):
    photo_name = image_url.split('/')[-1]

    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True

        image_folder = 'Photos'
        image_folder_path = os.path.join(get_project_root(), image_folder)
        photo_name += suffix if '.' not in photo_name else ''
        time_stamp = int(time.time())
        file_name = f'{time_stamp}_{photo_name}'
        Path(image_folder_path).mkdir(parents=True, exist_ok=True)
        file_path = os.path.join(image_folder_path, file_name)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        return file_path
    else:
        print(f'request error: {r.status_code}')


if __name__ == '__main__':
    download_image('https://picsum.photos/200')

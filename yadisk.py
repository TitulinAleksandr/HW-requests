from pprint import pprint
from wsgiref import headers
import requests

class YandexDisk:
    host = 'https://cloud-api.yandex.net'
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
    
    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'fields': 'name'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def _get_upload_link(self, disk_file_path):
        upload_url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': True}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()
    
    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        headers = self.get_headers()
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success') 

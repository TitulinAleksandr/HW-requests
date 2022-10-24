import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
hero_names = ['Hulk', 'Captain America', 'Thanos']
all_heroes = response.json()
our_heroes = filter(lambda hero: hero['name'] in hero_names, all_heroes)
intel = max({hero['name']: hero['powerstats']['intelligence'] for hero in our_heroes})
print(f'Самый умный супергерой {intel}')


from yadisk import YandexDisk

if __name__ == '__main__':
    with open(r'd:/New/HW requests/yankey.txt') as file:
        TOKEN = file.read()
    with open(r'd:/New/HW requests/text.txt') as file:
        disk_file_path = file.read()
    yadisk = YandexDisk(token=TOKEN)
    yadisk.get_files_list()
    yadisk._get_upload_link(disk_file_path)
    yadisk.upload_file_to_disk('/new/text.txt', 'text.txt')
    
 
    

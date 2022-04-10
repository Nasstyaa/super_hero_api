import requests


def get_name(url):
    res = requests.get(url)
    intelligence_level = res.json()['results'][0]['powerstats']['intelligence']
    hero_name = res.json()['results'][0]['name']

    new_dict = {}
    new_dict[hero_name] = int(intelligence_level)

    return new_dict


a = get_name('https://superheroapi.com/api/2619421814940190/search/Thanos')

b = get_name('https://superheroapi.com/api/2619421814940190/search/Hulk')

c = get_name('https://superheroapi.com/api/2619421814940190/search/Captain%America')

a.update(c)
a.update(b)

max_val = max(a, key=a.get)

print(f'Герой с максимальным уровнем интелекта: {max_val}')
import requests
from pyfiglet import Figlet
import folium


def get_ip_info(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            'IP': response.get('query'),
            'Prov': response.get('isp'),
            'Org': response.get('org'),
            'Country': response.get('country'),
            'Region Name': response.get('regioneName'),
            'City': response.get('city'),
            'ZIP': response.get('zip'),
            'LAT': response.get('lat'),
            'LON': response.get('lon')
        }
        for key, value in data.items():
            print(f'{key} : {value}')

        map_data = folium.Map(location=[response.get('lat'), response.get('lon')], zoom_start=15)

        map_data.save(f"{response.get('lat')}_{response.get('lon')}.html")

    except requests.exceptions.ConnectionError:
        print('Please, check your target IP')


def main():
    preview = Figlet(font='slant')
    print(preview.renderText('GET IP INFO'))
    ip = input('Please enter your target IP: ')

    get_ip_info(ip=ip)


if __name__ == '__main__':
    main()

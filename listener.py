import webbrowser
from time import sleep

import requests


VICTORY_URL = 'https://www.youtube.com/watch?v=eBShN8qT4lk'
ELIGIBILITY_URL = 'https://www.cvs.com/vaccine/intake/store/cvd-schedule.html?icid=coronavirus-lp-vaccine-sd-statetool'
SLEEP_SECONDS = .5


def check_zone_availability(zone):
    return zone['status'].lower() == 'available'


def listen():
    availability_url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.json'
    # or this one: https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    response = requests.get(
        availability_url,
        headers=headers,
        verify=False
    )
    if response.status_code != 200:
        return

    michigan_content = response.json()['responsePayloadData']['data']['MI']
    detroit_content = {}
    target_cities = ['detroit', 'grosse pointe']
    is_available = False
    for zone in michigan_content:
        if zone['city'].lower() in target_cities and check_zone_availability(zone):
            is_available = True
            print(f"Availability in {zone['city']}!")
            break

    return is_available


is_victory = False
counter = 0
while not is_victory:
    sleep(SLEEP_SECONDS)
    counter += 1
    is_victory = listen()

print('Huzzah!')
# webbrowser.open(ELIGIBILITY_URL)
webbrowser.open(VICTORY_URL)
print(f'That took {counter} attempts')

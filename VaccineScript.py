import requests
import time
from datetime import date

today = date.today()
print("Today date is: ", today)
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
current_date=reverse(today)

district = 152
date_day = current_date


URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    district, date_day)


header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}


def availability():
    counter = 0
    result = requests.get(URL, headers=header)
    print(result.status_code)
    result_json = result.json()
    data = result_json['sessions']
    for each_data in data:
        if((each_data['available_capacity'] > 0) & (each_data['min_age_limit'] == 45)):
            counter = +1
            print(each_data['name'])
            
            print(each_data['pincode'])
            print(each_data['vaccine'])
            print(each_data['available_capacity'])

        if(counter == 0):
            print('vaccine not available')
            return False


while(availability != True):
    time.sleep(2)
    availability()

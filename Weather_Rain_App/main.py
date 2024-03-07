import requests
import os

API_KEY = os.environ.get('OWM_API_KEY')
MY_LAT = os.environ.get('MY_LAT_LOC')
MY_LONG = os.environ.get('MY_LONG_LOC')

params = {
    'appid': API_KEY,
    'lat': MY_LAT,
    'lon': MY_LONG,
    'cnt': 4
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=params)
response.raise_for_status()
data = response.json()
# print(data['list'][0]['weather'][0]['id'])
def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get('telegram_bot_token')
    bot_chatID = os.environ.get('telegram_bot_chatid')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)

will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    telegram_bot_sendtext("Bring an umbrella! It's going to rain today")
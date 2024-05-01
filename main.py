import requests
import config
MY_LAT = 51.507351
MY_LNG = -0.127758
parameters = {
    "appid": config.OWM_API_KEY,
    "lat": MY_LAT,
    "lon": MY_LNG,
    "cnt": 4
}
response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
# Check for umbrella
bring_umbrella = False
for ele in data['list']:
    if ele['weather'][0]['id'] < 700:
        print("Bring your umbrella")
        bring_umbrella = True
        break
if not bring_umbrella:
    print("You are good")


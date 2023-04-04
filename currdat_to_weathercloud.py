import requests
import time
from datetime import datetime

# Weathercloud keys
weathercloudID = "Your Weathercloud ID"
weathercloudAPIKey = "Your Weathercloud API Key"

# Path to currdat.lst
currdat_path = "c:\programdata\currdat.lst"

# Update interval in seconds
update_interval = 11 * 60



#---------------------------------------
# function to read data from currdat.lst
def read_data(filename):
    data = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1]
                data[section] = {}
            elif "=" in line and line.count('=') == 1:
                key, value = line.split("=")
                data[section][key] = value.strip('"')
    return data


# function to send data to Weathercloud
def send_data(id_key, api_key, data):
    url = "https://api.weathercloud.net/v01/set"
    url += "?wid=" + id_key
    url += "&key=" + api_key
    dt = int(data["time"]["last_actualisation"])
    dt = datetime.fromtimestamp(dt - 2208988800)
    url += "&date=" + dt.strftime('%Y%m%d')
    url += "&time=" + dt.strftime('%H%M')
    url += "&temp=" + str(round(float(data["outdoor_temperature"]["deg_C"])*10))
    url += "&heat=" + str(round(float(data["outdoor_temperature"]["deg_C"])*10))
    url += "&tempin=" + str(round(float(data["indoor_temperature"]["deg_C"])*10))
    url += "&hum=" + data["outdoor_humidity"]["percent"]
    url += "&humin=" + data["indoor_humidity"]["percent"]
    url += "&wspd=" + str(round(float(data["wind_speed"]["mps"])*10))
    url += "&wdir=" + str(round(float(data["wind_direction"]["deg"])))
    url += "&rain=" + str(round(float(data["rain_24h"]["mm"])*10))
    url += "&rainrate=" + str(round(float(data["rain_1h"]["mm"])*10))
    url += "&bar=" + str(round(float(data["pressure_relative"]["hpa"])*10))
    url += "&dew=" + str(round(float(data["dewpoint"]["deg_C"])*10))
    url += "&chill=" + str(round(float(data["windchill"]["deg_C"])*10))

    response = requests.post(url)
    if response.status_code == 200:
        # data sent successfully to Weathercloud
        print("Data sent successfully to Weathercloud : " + dt.strftime('%m-%d-%Y %H:%M:%S'))
    elif response.status_code == 401:
        # authentication error
        print("Weathercloud authentication error : check your ID and API key")
    elif response.status_code == 429:
        # too many requests
        print("Too many requests")
    else:
        print("Error: {}".format(response.status_code))



# loop to send data to Weathercloud every update_interval
while True:
    # Read data from currdat.lst
    data = read_data(currdat_path)
    # Send data to Weathercloud
    send_data(weathercloudID, weathercloudAPIKey, data)
    # Wait for next update
    time.sleep(update_interval)
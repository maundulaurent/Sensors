from django.shortcuts import render
import requests
from datetime import datetime

# Function to fetch data from URL
def fetch_sensor_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None

# Function to get the latest entry from sensor data
def get_latest_entry(sensor_data):
    if sensor_data and 'results' in sensor_data and sensor_data['results']:
        results = sensor_data['results']
        latest_entry = max(results, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ'))
        return latest_entry
    else:
        return None

# Function to present the latest entry
def present_latest_entry(sensor_name, entry):
    if entry:
        return {
            'sensor_name': sensor_name,
            'timestamp': entry['timestamp'],
            'sensor_values': entry['sensordatavalues']
        }
    else:
        return None

def home(request):
    # URLs for sensor data
    sensor_urls = {
        "Sensor 41": [
            "https://api.sensors.africa/v1/data/?sensor=908&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=909&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=910&timestamp=&timestamp__gte=&timestamp__lte="
        ],
        "Sensor 51": [
            "https://api.sensors.africa/v1/data/?sensor=836&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=837&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=838&timestamp=&timestamp__gte=&timestamp__lte="
        ],
        "Sensor 61": [
            "https://api.sensors.africa/v1/data/?sensor=896&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=897&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=898&timestamp=&timestamp__gte=&timestamp__lte="
        ],
        "Sensor 81": [
            "https://api.sensors.africa/v1/data/?sensor=4889&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=4888&timestamp=&timestamp__gte=&timestamp__lte=",
            "https://api.sensors.africa/v1/data/?sensor=4890&timestamp=&timestamp__gte=&timestamp__lte="
        ] 
    }

    sensor_data_list = []
    for sensor_name, urls in sensor_urls.items():
        sensor_data = []
        for url in urls:
            data = fetch_sensor_data(url)
            latest_entry = get_latest_entry(data)
            if latest_entry:
                sensor_data.append(present_latest_entry(sensor_name, latest_entry))
        sensor_data_list.append(sensor_data)

    return render(request, 'display/sensor_data.html', {'sensor_data_list': sensor_data_list})

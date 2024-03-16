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
        print(f"Latest Sensor {sensor_name} Reading:")
        print("Timestamp:", entry['timestamp'])
        print("Sensor Data Values:")
        for sensor_value in entry['sensordatavalues']:
            print("ID:", sensor_value['id'])
            print("Value:", sensor_value['value'])
            print("Value Type:", sensor_value['value_type'])
        print()  # Add a newline for readability
    else:
        print(f"No data available for {sensor_name} sensor")

# URLs for sensor data
urls = {
    "Sensor 1": "https://api.sensors.africa/v1/data/?sensor=896&timestamp=&timestamp__gte=&timestamp__lte=",
    "Sensor 2": "https://api.sensors.africa/v1/data/?sensor=4890&timestamp=&timestamp__gte=&timestamp__lte=",
    "Sensor 3": "https://api.sensors.africa/v1/data/?sensor=918&timestamp=&timestamp__gte=&timestamp__lte="
}

def func():
    for sensor_name, url in urls.items():
        print(f"Fetching data from {url}...")
        sensor_data = fetch_sensor_data(url)
        latest_entry = get_latest_entry(sensor_data)
        if latest_entry:
            present_latest_entry(sensor_name, latest_entry)
            # Print data
            print(f"Sensor {sensor_name} Reading:")
            print(f"Timestamp: {latest_entry['timestamp']}")
            for sensor_value in latest_entry['sensordatavalues']:
                print(f"ID: {sensor_value['id']}")
                print(f"Value: {sensor_value['value']}")
                print(f"Value Type: {sensor_value['value_type']}")
            print()  # Empty line for separation
        else:
            print(f"No data available for {sensor_name} sensor")

# Call the function
func()

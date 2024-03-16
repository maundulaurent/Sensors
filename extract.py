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
    # "Sensor 2": "https://api.sensors.africa/v1/data/?sensor=4890&timestamp=&timestamp__gte=&timestamp__lte=",
    # "Sensor 3": "https://api.sensors.africa/v1/data/?sensor=918&timestamp=&timestamp__gte=&timestamp__lte="
}

# Open a file to write data
with open("sensor_data.txt", "w") as file:
    for sensor_name, url in urls.items():
        print(f"Fetching data from {url}...")
        sensor_data = fetch_sensor_data(url)
        latest_entry = get_latest_entry(sensor_data)
        if latest_entry:
            present_latest_entry(sensor_name, latest_entry)
            # Write data to file
            file.write(f"Sensor {sensor_name} Reading:\n")
            file.write(f"Timestamp: {latest_entry['timestamp']}\n")
            for sensor_value in latest_entry['sensordatavalues']:
                file.write(f"ID: {sensor_value['id']}\n")
                file.write(f"Value: {sensor_value['value']}\n")
                file.write(f"Value Type: {sensor_value['value_type']}\n")
            file.write("\n")
        else:
            print(f"No data available for {sensor_name} sensor")

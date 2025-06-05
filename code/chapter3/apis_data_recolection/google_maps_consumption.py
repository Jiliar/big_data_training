import requests

URL = "https://maps.googleapis.com/maps/api/directions/json"
GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your actual API key

params = {
    "origin": "New York, NY",
    "destination": "Los Angeles, CA",
    "mode": "driving",
    "key": GOOGLE_MAPS_API_KEY  # Replace with your actual API key
}

response = requests.get(URL, params=params)
if response.status_code == 200:
    data = response.json()
    if data["status"] == "OK":
        routes = data["routes"]
        for route in routes:
            print(f"Route summary: {route['summary']}")
            for leg in route["legs"]:
                print(f"Distance: {leg['distance']['text']}, Duration: {leg['duration']['text']}")
    else:
        print(f"Error in response: {data['status']}")
else:
    print(f"HTTP error: {response.status_code}")
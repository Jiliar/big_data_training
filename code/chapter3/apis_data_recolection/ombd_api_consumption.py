import requests

OBMD_API_URL = "http://www.omdbapi.com/"
API_KEY = 'ca919df0'

url = f"{OBMD_API_URL}?apikey={API_KEY}&t=matrix&y=2025&plot=full"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Response from OMDB API: {data}")
    if data["Response"] == "True":
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Director: {data['Director']}")
        print(f"Plot: {data['Plot']}")
    else:
        print(f"Error in response: {data['Error']}")
else:
    print(f"HTTP error: {response.status_code}")
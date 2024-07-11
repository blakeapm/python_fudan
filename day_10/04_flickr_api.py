import datetime
import getpass
import requests

def get_date_string(date_string):
    dt = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    unix_timestamp = int(dt.timestamp())
    unix_date = str(unix_timestamp)
    return unix_date

def search_flickr_images(lat, lon, date_start, date_end, radius=.1, per_page=10, page=1):
    base_url = 'https://www.flickr.com/services/rest/'
    params = {
        'method': 'flickr.photos.search',
        'api_key': API_KEY,
        'lat': lat,
        'lon': lon,
        'min_upload_date': date_start,
        'max_upload_date': date_end,
        'radius': radius,
        'per_page': per_page,
        'page': page,
        'format': 'json',
        'nojsoncallback': 1
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['stat'] == 'ok':
            return data['photos']['photo']
        else:
            print(f"Error: {data['message']}")
            return []
    else:
        print(f"HTTP Error: {response.status_code}")
        return []

def construct_image_url(p):
    s = p['server']
    pid = p['id']
    ps = p['secret']
    return f"https://live.staticflickr.com/{s}/{pid}_{ps}.jpg"

API_KEY = getpass.getpass(prompt="Enter your API key: ")

if __name__ == "__main__":
    lat = input("Search lat: ")
    lon = input("Search lon: ")
    date_start = get_date_string(input("Search date start (YYYY-MM-DD): "))
    date_end = get_date_string(input("Search date end (YYYY-MM-DD): "))

    photos = search_flickr_images(lat, lon, date_start, date_end)
    if photos:
        print("Found photos:")
        for photo in photos:
            print(f"Title: {photo['title']}")
            print(f"URL: {construct_image_url(photo)}\n")
    else:
        print("No photos found.")

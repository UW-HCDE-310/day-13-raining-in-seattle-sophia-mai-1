import json
import urllib.request

class AstroPhoto:
  def __init__(self, data):
    self.title = data["title"]
    self.date = data["date"]
    self.description = data["explanation"]
    self.url = data["hdurl"]

  def get_short_description(self):
    if len(self.description) <= 200:
      return self.description
    else:
      return (self.description[0:197] + "...")

def get_apod(api_key, date=None):
  url = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key)
  if date:
    url += "&date={}".format(date)
  with urllib.request.urlopen(url) as request:
    response = request.read().decode()
  return AstroPhoto(json.loads(response))

def get_random_apods(api_key, count):
  url = "https://api.nasa.gov/planetary/apod?api_key={}&count={}".format(api_key, count)
  with urllib.request.urlopen(url) as request:
    response = request.read().decode()
  photos = []
  for item in json.loads(response):
    photos.append(AstroPhoto(item))
  return photos

def get_apods_between(api_key, start_date, end_date):
  url = "https://api.nasa.gov/planetary/apod?api_key={}&start_date={}&end_date={}".format(api_key, start_date, end_date)
  with urllib.request.urlopen(url) as request:
    response = request.read().decode()
  photos = []
  for item in json.loads(response):
    photos.append(AstroPhoto(item))
  return photos

# Example usage (replace "DEMO_KEY" with your actual API key)
apod_instance = get_apod("DEMO_KEY")
print("Today's APOD title:", apod_instance.title)
print("Short description:", apod_instance.get_short_description())

# Get random APODs
random_apods = get_random_apods("DEMO_KEY", 2)
print("Number of random APODs retrieved:", len(random_apods))

# Get APODs between specific dates (e.g., January 1st to 7th, 2023)
apods_between = get_apods_between("DEMO_KEY", "2023-01-01", "2023-01-07")
print("Number of APODs between specified dates:", len(apods_between))
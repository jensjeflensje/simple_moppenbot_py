import requests

def get_random_joke():
    r = requests.get("https://moppenbot.nl/api/random")
    if r.status_code == 200:
        return r.json()["joke"]
    else:
        raise Exception("HTTP request failed")
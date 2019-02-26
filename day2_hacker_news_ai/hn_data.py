import json
import requests
import os


def download_hn_data(filename):
    data = []
    for i in range(10):
        url = f"https://api.hnpwa.com/v0/news/{i + 1}.json"
        print(f"Downloading {url}...")
        r = requests.get(url)
        data.extend(r.json())
    with open(filename, 'w') as f:
        json.dump(data, f)
        return data


def read_hn_data_from_file(filename):
    with open(filename) as f:
        return json.load(f)


def load_data():
    filename = "hn_data.json"
    if os.path.exists(filename):
        return read_hn_data_from_file(filename)
    else:
        return download_hn_data(filename)

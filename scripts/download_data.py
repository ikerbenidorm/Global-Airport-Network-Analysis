import os
import requests

# URLs datasets of OpenFlights
urls = {
    "airports.dat": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat",
    "routes.dat": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat",
    "airlines.dat": "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat"
}

# Directory where data will be saved
raw_data_dir = "../data/raw"

# Create the folder if it doesn't exist
os.makedirs(raw_data_dir, exist_ok=True)

def download_file(url, filepath):
    try:
        print(f"Downloading {url} ...")
        response = requests.get(url)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"Saved to: {filepath}\n")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    for filename, url in urls.items():
        filepath = os.path.join(raw_data_dir, filename)
        download_file(url, filepath)

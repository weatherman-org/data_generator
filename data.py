import requests
from tqdm import tqdm
import pandas as pd
import sys

def download_csv(url: str, params: dict, filename: str) -> bool:
    print("Starting download...")
    try:
        with requests.get(url, params=params, stream=True) as response:
            if response.status_code == 200:
                total_size_in_bytes = int(response.headers.get('content-length', 0))
                with open(filename, 'wb') as file, tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, miniters=1, desc="Downloading...") as pbar:
                    for data in response.iter_content(1024):  # Processing the stream in 1KB chunks
                        file.write(data)
                        pbar.update(len(data))
                print(f"Download completed successfully. File saved as: {filename}")
                return True
            else:
                print(f"Request failed with status code: {response.status_code}")
                return False
    except Exception as e:
        print(f"An error occurred during the download: {e}")
        return False

def pre_process(filename: str):
    print(f"Starting pre-processing on {filename}...")
    try:
        # Attempt to read the CSV file
        data = pd.read_csv(filename, skiprows=3)
        print("Data loaded into DataFrame.")

        # Rename the columns as specified
        data.rename(inplace=True, columns={
            "temperature_2m (°C)": "temperature",
            "relative_humidity_2m (%)": "humidity",
            "rain (mm)": "water_amount",
            "surface_pressure (hPa)": "pressure",
            "wind_speed_100m (km/h)": "wind_speed",
            "wind_direction_100m (°)": "wind_direction"
        })

        print("Columns renamed successfully.")

        # Overwrite the original file with the processed data
        data.to_csv(filename, index=False)
        print(f"Processed data saved to {filename}")

    except pd.errors.EmptyDataError:
        print("The file is empty. No data to process.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during pre-processing: {e}")
        sys.exit(1)

def process():
    # Define the URL, parameters, and filename
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 12.9184,
        "longitude": 79.1325,
        "start_date": "2003-01-01",
        "end_date": "2024-01-01",
        "hourly": "temperature_2m,relative_humidity_2m,rain,surface_pressure,wind_speed_100m,wind_direction_100m",
        "timezone": "auto",
        "format": "csv"
    }
    filename = "data.csv"

    # Download the CSV data
    if download_csv(url, params, filename):
        # Pre-process the downloaded CSV data only if download was successful
        pre_process(filename)
    else:
        print("Download was not successful. Pre-processing step will be skipped.")
        sys.exit(1)  # Exit with error status if download failed
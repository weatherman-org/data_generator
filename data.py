"""
This script automates the process of downloading weather data in CSV format from a specified URL,
then preprocesses the downloaded file to rename certain columns for consistency and readability.
"""

import requests
from tqdm import tqdm
import pandas as pd
import sys
import os

def download_csv(url: str, params: dict, filename: str) -> bool:
    """
    Downloads a CSV file from a specified URL with given parameters.

    Parameters:
    - url (str): The URL from which to download the CSV file.
    - params (dict): A dictionary of parameters to pass along with the request.
    - filename (str): The name of the file to save the downloaded content.

    Returns:
    - bool: True if the download was successful, False otherwise.
    """
    print("Starting download...")
    try:
        # Send a GET request to the specified URL with the given parameters
        with requests.get(url, params=params, stream=True) as response:
            if response.status_code == 200:
                # Obtain the total size of the file to be downloaded
                total_size_in_bytes = int(response.headers.get('content-length', 0))
                # Open the file and write the content in chunks, showing progress
                with open(filename, 'wb') as file, tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, miniters=1, desc="Downloading...") as pbar:
                    for data in response.iter_content(1024):  # 1KB chunks
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
    """
    Pre-processes the downloaded CSV file by renaming specified columns.

    Parameters:
    - filename (str): The name of the file to preprocess.
    """
    print(f"Starting pre-processing on {filename}...")
    try:
        # Load the CSV data into a DataFrame, skipping the first 3 rows
        data = pd.read_csv(filename, skiprows=3)
        print("Data loaded into DataFrame.")

        # Rename columns according to specified mappings
        data.rename(inplace=True, columns={
            "temperature_2m (°C)": "temperature",
            "relative_humidity_2m (%)": "humidity",
            "rain (mm)": "water_amount",
            "surface_pressure (hPa)": "pressure",
            "wind_speed_100m (km/h)": "wind_speed",
            "wind_direction_100m (°)": "wind_direction"
        })
        print("Columns renamed successfully.")

        # Save the processed data back to the same file
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

def main():
    """
    Main function to orchestrate the downloading and pre-processing of weather data.
    """
    # Configuration for data download
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 12.9184,
        "longitude": 79.1325,
        "start_date": os.getenv("START_DATE"),
        "end_date": os.getenv("END_DATE"),
        "hourly": "temperature_2m,relative_humidity_2m,rain,surface_pressure,wind_speed_100m,wind_direction_100m",
        "timezone": "auto",
        "format": "csv"
    }
    filename = "data.csv"

    # Attempt to download the CSV data
    if download_csv(url, params, filename):
        # Proceed to pre-process the data if download was successful
        pre_process(filename)
    else:
        print("Download was not successful. Pre-processing step will be skipped.")
        sys.exit(1)

if __name__ == "__main__":
    main()

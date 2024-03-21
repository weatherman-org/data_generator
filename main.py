import generated.weather_telemetry_pb2 as weather_telemetry_pb2
import paho.mqtt.client as mqtt
import time
import pandas as pd
import sys
import data
HOST = "emqx"
TOPIC = "topic/telemetry"
PORT = 1883
INTERVAL = 60*60  # This is used for an additional delay between messages.

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")
        client.loop_stop()  # Stop the loop on failure to connect
        sys.exit(1)

def on_disconnect(client, userdata, rc, properties,flags):
    if rc != 0:  # If rc is 0, the disconnection was expected
        print("Unexpected disconnection.")
    print("Disconnected from MQTT Broker")

def setup_mqtt_client():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(HOST, PORT)
    client.loop_start()
    return client

def publish_weather_data(client, data_file):
    try:
        data = pd.read_csv(data_file)
        if data.empty:
            print("Data file is empty. Exiting...")
            sys.exit(1)
    except FileNotFoundError:
        print("Data file not found. Exiting...")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Data file is empty or invalid. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data file: {e}")
        sys.exit(1)

    try:
        for _, row in data.iterrows():
            weather_data = weather_telemetry_pb2.WeatherTelemetry()
            weather_data.temperature = row['temperature']
            weather_data.humidity = row['humidity']
            weather_data.windSpeed = row['wind_speed']
            weather_data.windDirection = row['wind_direction']
            weather_data.pressure = row['pressure']
            weather_data.waterAmount = row['water_amount']
            row_time = pd.to_datetime(row["time"])
            weather_data.timestamp = int(row_time.timestamp() * 1000)

            serialized_data = weather_data.SerializeToString()
            client.publish(TOPIC, serialized_data)
            print(f"Published data for {row_time} to {TOPIC}.")

            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Publication interrupted by user.")
    except Exception as e:
        print(f"An error occurred during publication: {e}")

def main():
    data.process()
    client = setup_mqtt_client()
    try:
        publish_weather_data(client, "data.csv")
    finally:
        client.loop_stop()
        client.disconnect()
        print("Program exited gracefully.")

if __name__ == "__main__":
    main()

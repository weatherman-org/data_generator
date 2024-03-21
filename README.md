# Weather Telemetry Data Pipeline

This project implements a complete pipeline for fetching, processing, and publishing weather telemetry data to an MQTT broker, utilizing Protobuf for data serialization. It also demonstrates setting up a PostgreSQL database and an MQTT broker (EMQX) using Docker.

## Components

- **Data Fetching and Processing**: Downloads weather data in CSV format, preprocesses it, and saves it for publishing.
- **MQTT Publisher**: Reads the preprocessed data and publishes it to an MQTT broker using the Protobuf format.
- **Docker Environment**: Contains the setup for the MQTT broker (EMQX), PostgreSQL database, and the application itself.

## Prerequisites

- Docker and Docker Compose
- Python 3.11.5 or newer
- Paho MQTT Python client
- Pandas library
- Protobuf compiler and Python library

## Setup and Running

### Environment Variables

Make sure to set the following environment variables either directly or through a `.env` file:

- `INTERVAL`: Publishing interval in seconds.
- `START_DATE`: Start date for fetching weather data.
- `END_DATE`: End date for fetching weather data.

### Building the Docker Image

To build the Docker image for the data generator application, navigate to the project directory and run:

```sh
docker build -t data-generator:latest .

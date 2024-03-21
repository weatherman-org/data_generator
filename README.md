# Weather Telemetry Data System

This project establishes a robust pipeline for the collection, processing, and dissemination of weather telemetry data. Utilizing Docker for streamlined deployment, the system integrates a set of services including a data generator, an MQTT broker, a data-consuming server, and a PostgreSQL database. This setup facilitates the seamless flow of weather data from acquisition to storage, ideal for applications in data analytics, monitoring, or environmental research.

## Components Overview

- **Data Generator**: Downloads, processes, and publishes weather data to an MQTT broker based on specified start and end dates.
- **MQTT Broker (EMQX)**: Facilitates real-time messaging between the data generator and the server.
- **PostgreSQL Database**: Stores the processed weather data for persistent access and analysis.
- **Server**: Subscribes to the MQTT broker to receive weather data, which it then processes and stores in the database.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system.
- Basic familiarity with Docker containerization concepts.

### Building and Running the System

1. **Build the Data Generator Docker Image**

   Given that `START_DATE` and `END_DATE` are build-time variables, use the `--build-arg` option with `docker build`:

   ```bash
   docker build --build-arg START_DATE=2003-01-01 --build-arg END_DATE=2024-01-01 -t data-generator:latest .
   ```

2. **Configure the System**

   Modify the `.env` file or the docker-compose.yml directly to adjust environment variables and settings according to your needs. Ensure that the `START_DATE` and `END_DATE` variables match your requirements.

3. **Deploy with Docker Compose**

   Launch all services with the following command:

   ```bash
   docker-compose up -d
   ```

This spins up the necessary infrastructure, initiating the automatic data flow from the data generator through to data storage in PostgreSQL.

### System Interaction

- **Data Generation**: The data generator simulates telemetry collection by fetching, preprocessing, and publishing serialized weather data.
- **Data Consumption**: The server listens for new data on the MQTT topic, deserializes the payloads, and persists them in the PostgreSQL database.

## Docker Build Dependencies

Note that compiling certain Python packages for the data generator might necessitate additional build-time dependencies. You may need to extend the Dockerfile to include the necessary packages for your Python environment, particularly when using Alpine Linux as the base image.
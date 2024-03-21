# Use Python 3.11.5 Alpine image
FROM python:3.11.5-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY ./requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
ARG START_DATE
ARG END_DATE
ENV INTERVAL=3600
ENV START_DATE=${START_DATE}
ENV END_DATE=${END_DATE}
COPY ./data.py ./data.py
COPY ./main.py ./main.py
COPY ./generated ./generated
RUN python ./data.py
CMD ["python", "./main.py"]

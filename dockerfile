FROM python:3.11.5-alpine
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV INTERVAL=3600
ENV START_DATE=2003-01-01
ENV END_DATE=2024-01-01
COPY ./data.py ./data.py
COPY ./main.py ./main.py
COPY ./generated ./generated
RUN python ./data.py
CMD ["python", "./main.py"]

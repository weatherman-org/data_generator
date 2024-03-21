FROM python:3.11.5-alpine
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./data.py ./data.py
COPY ./main.py ./main.py
COPY ./generated ./generated
CMD ["python", "./main.py"]

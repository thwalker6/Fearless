FROM python:3.8.5

WORKDIR /fearless-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./itemsAPI ./itemsAPI

CMD ["python", "./itemsAPI/main.py"]
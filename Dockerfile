FROM python:3.11

WORKDIR /app

COPY ./requirements/ requirements/

RUN pip install --no-cache-dir -r /app/requirements/base.txt

COPY . /app/

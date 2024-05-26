FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    git clone https://github.com/vishnubob/wait-for-it.git

COPY . /app/
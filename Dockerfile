FROM python:3.8
COPY . /random_dress_bot/

WORKDIR /random_dress_bot

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir bs4
RUN pip install --no-cache-dir pyTelegramBotAPI
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir lxml
RUN pip install psycopg2

CMD python bot.py
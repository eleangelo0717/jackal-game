FROM python:3.6

RUN python -m pip install requests python-dotenv python-telegram-bot PySocks python-telegram-bot[socks]

COPY . /app

WORKDIR /app

CMD ["python", "app.py"]
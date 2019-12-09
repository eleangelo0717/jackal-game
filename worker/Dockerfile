FROM python:3.6

RUN python -m pip install Pillow numpy lxml requests python-dotenv

COPY images /app/images/
COPY *.py /app/

WORKDIR /app

CMD ["python", "app.py"]
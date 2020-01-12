FROM python:alpine 

COPY . /src/

RUN pip install -r /src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
FROM python:alpine 

COPY . /src/

RUN pip install -r /src/requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "/src/gameserver.py"]
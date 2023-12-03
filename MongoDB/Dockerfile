FROM python:3.8-alpine

RUN mkdir app
COPY requirements.txt /app/requirements.txt
COPY flask_MongoDB.py /app/flask_MongoDB.py
WORKDIR /app/

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "flask_MongoDB.py" ]
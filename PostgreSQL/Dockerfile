FROM python:3.8-alpine

RUN mkdir app
COPY requirements.txt /app/requirements.txt
COPY flask_PSQL.py /app/flask_PSQL.py
WORKDIR /app/

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "flask_PSQL.py" ]
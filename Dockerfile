#FROM python:3-alpine

#WORKDIR /fileapp

#COPY ./mount.py .

#COPY ./servers.txt .
#
#CMD ["python", "mount.py"]
FROM python:3.11-alpine

WORKDIR /myapp

COPY ./app.py .

RUN pip install pymysql

CMD [ "python" ,"app.py"]

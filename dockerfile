FROM ubuntu:16.04

MAINTAINER Your Name "jicowan@hotmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app.py /app/app.py

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

EXPOSE 5000
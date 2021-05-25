FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y procps
RUN apt-get install -y python3-dev libffi-dev libpq-dev gcc && pip3 install --upgrade pip
RUN apt-get install -y netcat

COPY ./requirements.txt /requirements.txt
COPY ./fixtures/initial_data.yaml /initial_data.yaml
RUN pip3 install --default-timeout=100  -r /requirements.txt

# Setup directory structure
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

COPY . /usr/src/app

# run server
CMD ["/usr/src/app/entrypoint.sh"]



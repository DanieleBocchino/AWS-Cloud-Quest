FROM python:3.8-slim-buster

MAINTAINER Your Name "test@test.com"

COPY ./ ./app
WORKDIR ./app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8443"]
FROM python:3-onbuild

ADD . /myapp

WORKDIR /myapp

RUN pip install --upgrade pip -r requirements.txt

EXPOSE 5000

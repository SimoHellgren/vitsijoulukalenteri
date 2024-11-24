FROM python:3.13

RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr

COPY . .
RUN pip install -r requirements.txt

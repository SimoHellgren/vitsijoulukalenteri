FROM python:3.13

RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "test.py" ]

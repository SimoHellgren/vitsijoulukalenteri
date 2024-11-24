FROM python:3.13

RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr

COPY src/requirements.txt src/requirements.txt
RUN pip install -r src/requirements.txt

COPY . .

ENTRYPOINT [ "python", "src/script.py" ]
CMD [ "test.jpg" ]

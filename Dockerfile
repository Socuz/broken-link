FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip
RUN pip3 install --upgrade pip

COPY ./ ./

RUN pip3 install -r requirements.txt

CMD ["python3", "/test.py"]
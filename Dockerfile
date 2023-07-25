FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip
RUN pip3 install --upgrade pip

RUN addgroup -S broken && adduser -S broken -G broken

RUN mkdir -p /opt/broken-link/ && chown broken:broken /opt/broken-link/

COPY --chown=broken:broken ./ ./opt/broken-link/
WORKDIR /opt/broken-link/
RUN pip3 install -r requirements.txt

USER broken
CMD ["python3", "/opt/broken-link/broken_ext_links.py"]
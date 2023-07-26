FROM alpine:latest

RUN apk add --update --no-cache python3 py3-pip
RUN pip3 install --upgrade pip

RUN addgroup -S broken && adduser -S broken -G broken

RUN mkdir -p /opt/broken-link/ && chown broken:broken /opt/broken-link/

USER broken
WORKDIR /opt/broken-link/
COPY --chown=broken:broken ./ ./
RUN chmod -R 775 .

USER root
RUN pip3 install -r requirements.txt

USER broken
CMD ["python3", "/opt/broken-link/broken_ext_links.py"]
FROM python:3.12-rc-alpine3.18

RUN pip install --upgrade pip

RUN adduser -D worker
USER worker
RUN mkdir -p /home/worker/broken-link/
WORKDIR /home/worker/broken-link
COPY --chown=worker:worker requirements.txt requirements.txt
COPY --chown=worker:worker broken_ext_links.py broken_ext_links.py

RUN pip install --user -r requirements.txt
ENV PATH="/home/worker/.local/bin:${PATH}"

CMD ["python", "/home/worker/broken-link/broken_ext_links.py"]
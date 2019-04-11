FROM python:2.7-slim

ENV TOKEN ''
ENV API_URL 'http://127.0.0.1:5000'

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app
RUN chmod +x /opt/app/run.sh

ENTRYPOINT ["./run.sh"]
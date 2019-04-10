FROM python:2.7.16-alpine3.8

ENV TOKEN 

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app

CMD ["python", "src/run_voucher_api.py", "--token=$TOKEN"]
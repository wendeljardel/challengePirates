FROM python:3.8.1-slim

ADD src/buscaCep.py /root/buscaCep.py
ADD test/test_buscaCep.py /root/test_buscaCep.py
ADD requirements.txt /root/requirements.txt

RUN pip install -r /root/requirements.txt

WORKDIR /root

CMD ["python", "buscaCep.py"]
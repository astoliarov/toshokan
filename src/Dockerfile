FROM python:3.6-alpine3.6
ENV PYTHONUNBUFFERED 1

# Зависимости для pycrypto
RUN apk --no-cache add g++ autoconf python-dev

RUN mkdir /config
RUN mkdir /code;

ADD ./requirements.txt /config/
ADD ./requirements-test.txt /config/

RUN pip install -r /config/requirements.txt
RUN pip install -r /config/requirements-test.txt

ADD . /code/

WORKDIR /code

CMD ["python", "run.py"]

FROM ubuntu:trusty

RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main" >> /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y git build-essential python python-dev python-distribute python-pip

RUN pip install virtualenv

RUN git clone https://github.com/brenda151295/Tweet_microservicios.git app

WORKDIR /app

RUN make install

RUN make createdb

EXPOSE 5001

CMD ["venv/bin/python", "services/tweet.py"]

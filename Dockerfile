FROM python:3.6.9

RUN apt-get -y update && apt-get install -y git nmap telnet vim

ENV APP_DIR /predictor
ENV VIRTUAL_ENV /predictor/venv
WORKDIR $APP_DIR

COPY requirements.txt .
COPY scripts/install_script.sh install_script.sh
RUN ./install_script.sh
EXPOSE 3002
COPY . /predictor
FROM ubuntu:18.04

# COPY ./config/ /opt/data/
COPY ./config/requirements_config.txt /opt/data/requirements_config.txt

RUN apt-get update && apt-get install -y \
  curl \
  python3 \
  python3-pip \
  firefox
RUN pip3 install -r /opt/data/requirements_config.txt
CMD bash /opt/data/config.sh
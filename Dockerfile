FROM python:3.7.12

RUN mkdir -p /data/apps/weather_service
RUN mkdir -p /data/logs

WORKDIR /data/apps/weather_service

RUN echo 'Asia/Shanghai' > /etc/timezone && /bin/ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY requirements.txt /data/apps/weather_service/

RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

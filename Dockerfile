FROM python:3.7.4
MAINTAINER Zheng zxyful@gmail.com

LABEL Version="1.0" \
      LastModifiedDate="2019-07-22"

ADD . /app/

WORKDIR /app/

COPY ./pip.conf /etc/pip.conf

# 时区设置
ENV TZ=Asia/Shanghai

RUN pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

#RUN chmod a+x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT gunicorn -c gunicorn.conf.py app:app
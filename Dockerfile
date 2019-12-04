FROM python:3.7.4
MAINTAINER Zheng zxyful@gmail.com

LABEL Version="2.0" \
      LastModifiedDate="2019-11-29"

ADD . /app/

WORKDIR /app/

COPY ./pip.conf /etc/pip.conf

# 时区设置
ENV TZ=Asia/Shanghai

RUN pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

#RUN chmod a+x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT gunicorn -c gunicorn.conf.py main:app

# 使用命令
# docker run -d -p 5000:5000 --restart=always registry.cn-hangzhou.aliyuncs.com/zxyle/spider_server
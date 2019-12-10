FROM python:3.7.4

ADD . /app/

WORKDIR /app/

COPY ./pip.conf /etc/pip.conf

# 时区设置
ENV TZ=Asia/Shanghai

RUN pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

# 使用命令
# docker run -d -p 5000:5000 --restart=always registry.cn-hangzhou.aliyuncs.com/zxyle/spider_server
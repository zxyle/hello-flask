# 哲象爬虫有关接口/flask server项目模板

## 简介
该项目基于python3的flask的web项目.

实现的技术
- 工厂模式结构
- 已支持nginx+gunicorn+docker部署


## 接口列表
* /oss/transfer POST 转存图片到oss


## 部署方式
docker-compose安装和文档 请参考docker官方文档
```
docker-compose up -d --build
```

## 关闭服务
```
docker-compose down -v --rmi all
```

* -v  删除volume
* --rmi 删除镜像
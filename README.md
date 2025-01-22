# 简介
基于selenium实现的爬虫系统，可以爬取wiley和sciencedirect上的文献信息，自动翻译后汇总成word文档发送到邮箱。本仓库提供了配置好环境的docker镜像，任何人都可以修改源码然后轻松部署。

通过本仓库，你可以参考：
- 基于selenium实现爬虫
- 基于baidu api实现实时翻译
- 基于docx生成word文档
- 基于smtplib自动发送邮件
# 如何使用
## 基于docker部署（推荐）
```
# 通过百度网盘下载镜像tar文件
https://pan.baidu.com/s/1OQJEcDK2rY2P3-vKQMAGOg?pwd=e95v

# 通过scp将tar文件拷贝到服务器上，这里假设拷贝到用户根目录
scp spider.tar root@server_ip:~/

# ssh登录服务器
ssh root@server_ip
cd ~

# 假设服务器已经安装了docker，从tar文件加载镜像
docker load -i spider.tar

# 假设服务器已经安装了git
git clone https://github.com/howard1209a/web_spider_academic.git

# 填入自己的配置，具体配置含义以及如何申请查看下文
vim ~/web_spider_academic/src/config.json

# 执行Dockerfile生成新镜像
cd ~/web_spider_academic
docker build -t web_spider_academic .

# 启动容器
docker run -d -p 5000:5000 web_spider_academic








```
## 裸机部署（配置环境繁琐）
## 修改源码并通过docker部署
# 配置文件
config.json配置文件
- sender_email：邮件发送者邮箱
- receiver_email：邮件接收者邮箱
- email_authorization_code：邮件发送者邮箱的校验码，具体查看方式参照下文博客
- baidu_translate_api_appid：百度翻译api的appid，具体申请方式参照下文博客
- baidu_translate_api_appkey：百度翻译api的appid，具体申请方式参照下文博客
# 系统设计
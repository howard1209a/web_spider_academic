FROM spider

WORKDIR /home/seluser/web_spider_academic

COPY . /home/seluser/web_spider_academic

RUN sudo chmod +x /home/seluser/web_spider_academic/run.sh

# 指定容器启动的默认命令
CMD ["/home/seluser/web_spider_academic/run.sh"]

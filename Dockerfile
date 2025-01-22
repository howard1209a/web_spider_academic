FROM spider

WORKDIR ~/web_spider_academic

COPY . ~/web_spider_academic

RUN chmod +x ~/web_spider_academic/run.sh

CMD ["~/web_spider_academic/run.sh"]

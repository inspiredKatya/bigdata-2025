FROM shvasily/hadoop:1.0.0

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 \
      python3-pip
ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

ADD run.sh /run.sh
RUN chmod a+x /run.sh
COPY entrypoint.sh /entrypoint.sh

EXPOSE 9870

ENTRYPOINT ["/run.sh"]



FROM shvasily/hadoop:1.0.0

HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1

ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data
RUN mkdir -p /hadoop/dfs/data
VOLUME /hadoop/dfs/data

COPY run.sh /run.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /run.sh

EXPOSE 9864
ENTRYPOINT ["/run.sh"]


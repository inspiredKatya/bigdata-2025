FROM shvasily/hadoop:1.0.0

HEALTHCHECK CMD curl -f http://localhost:8042/ || exit 1

ADD run.sh /run.sh
RUN chmod a+x /run.sh
COPY entrypoint.sh /entrypoint.sh

EXPOSE 8042

ENTRYPOINT ["/run.sh"]


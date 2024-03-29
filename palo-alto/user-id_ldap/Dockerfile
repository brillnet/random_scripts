FROM fluentd

USER root
RUN apk add --update --no-cache python3
RUN ln -sf python3 /usr/bin/python
RUN apk add --update --no-cache py3-pip
RUN pip3 install requests

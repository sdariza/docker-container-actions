FROM python:latest

COPY entrypoint.sh /
COPY main.py /python_run

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
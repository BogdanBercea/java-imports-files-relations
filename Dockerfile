FROM python:3.8-slim-buster

WORKDIR /plugin

COPY main.py ./main.py
COPY spring-boot ./spring-boot

CMD ["python3", "main.py", "results/dockerResults.json", "spring-boot"],
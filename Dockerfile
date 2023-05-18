FROM ubuntu:18.04

RUN apt update

CMD ["python3", "helloworld.py"]

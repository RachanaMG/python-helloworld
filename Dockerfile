FROM ubuntu:18.04

RUN apt update
RUN python3 --version

CMD ["python3", "helloworld.py"]

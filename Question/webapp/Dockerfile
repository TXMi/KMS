FROM nginx:1.15.8

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

FROM ubuntu:latest

RUN apt update && apt install  openssh-server sudo -y

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]

FROM python:3.8-slim-buster

RUN apt-get update -y

RUN apt-get install python -y

RUN apt-get install python-pip -y

RUN pip install flask

COPY . .

CMD [ "python", "./webapp/app.py"]
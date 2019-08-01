FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir /titanic
WORKDIR /titanic

COPY requirements.txt /titanic/
RUN pip install -r requirements.txt

COPY . /titanic/

EXPOSE $PORT

CMD ["/bin/bash","/titanic/docker_run.sh"]


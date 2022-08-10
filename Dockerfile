FROM python:3.6

ARG HOST
ARG group

ENV PYTHONUNBUFFERED 1
ENV DRIVER remote
WORKDIR /test_code
ADD requirements.txt /test_code/

RUN apt-get update -y && apt-get install -y build-essential libpoppler-cpp-dev pkg-config python-dev

RUN pip install --upgrade -r requirements.txt
ADD . /test_code/

CMD bash -c "python -m pytest -s tests --capture=tee-sys --driver Remote --selenium-host $HOST --selenium-port 4444 --capability browserName firefox"

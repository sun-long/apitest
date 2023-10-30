FROM python:3.8.16-slim-bullseye

#timezone config
RUN cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN mkdir /home/apitest

# create virtual env
RUN python3 -m venv /home/apitest/venv
ENV VIRTUAL_ENV=/home/apitest/venv
ENV PATH="/home/apitest/venv/bin:$PATH"

# install requirements pycrytodomex
RUN python3 -m pip install pycryptodomex
ENV PYTHONIOENCODING=utf-8

# install requirements
COPY requirements-ci.txt .
RUN pip3 install -i https://repo.sensetime.com/repository/pypi/simple --no-cache-dir -r requirements-ci.txt

RUN mkdir /home/apitest/code
WORKDIR /home/apitest/code
COPY . .
ENV PYTHONIOENCODING=utf-8
# ENTRYPOINT ["pytest","-sv"]

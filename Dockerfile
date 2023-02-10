FROM python:3.9
WORKDIR /repository
COPY . .
RUN apt update -y
RUN apt install -y libpq-dev gdb
RUN pip install -r requirements.txt
RUN pip install pydantic[dotenv] pydevd-pycharm

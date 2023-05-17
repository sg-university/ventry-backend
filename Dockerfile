FROM python:3.11
WORKDIR /app
COPY . .
RUN apt update -y
RUN apt install -y libpq-dev gdb
RUN pip install -r requirements.txt
RUN pip install pydantic[dotenv] aiopg[sa] pydevd-pycharm sqlalchemy[asyncio]

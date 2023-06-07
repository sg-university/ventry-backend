FROM python:3.11
WORKDIR /app
COPY . .
RUN apt update -y
RUN pip install -r requirements.txt
RUN pip install pydantic[dotenv] aiopg[sa] sqlalchemy[asyncio]
CMD uvicorn app.main:app --host 0.0.0.0 --port 8080 --workers 1
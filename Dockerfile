# Initialize the base image.
FROM nvidia/cuda:11.3.0-base-ubuntu20.04


# Set the working directory.
WORKDIR /app
COPY . .

# Install dependencies.
RUN apt update -y
RUN yes | DEBIAN_FRONTEND=noninteractive apt install -y libpq-dev gdb python3 python3-pip
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install torch==1.13.1+cu116 torchvision==0.14.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip3 install -r requirements.txt
RUN pip3 install pydantic[dotenv] aiopg[sa] pydevd-pycharm sqlalchemy[asyncio]

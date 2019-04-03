#Using Python 3
FROM python:3.8-rc
ENV PYTHONUNBUFFERED 1

#work directory
WORKDIR /code

COPY requirements.txt /code/

#install requirements
RUN pip install -U -r requirements.txt

COPY . ./
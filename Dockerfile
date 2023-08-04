# Use an official Python runtime as a parent image
FROM python:3

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

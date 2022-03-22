# syntax=docker/dockerfile:1

FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=1
ENV SECRET_KEY=django-insecure-jh!y^h#52+3l^+fm@(fph+a3kks-%y9i1&$k4_zas*imsvd79u
WORKDIR /django
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

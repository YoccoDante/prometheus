# syntax=docker/dockerfile:1
FROM python:3.7-alpine

WORKDIR /app

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=true

RUN apk add --no-cache gcc musl-dev linux-headers

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
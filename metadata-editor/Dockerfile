FROM python:3.8.10-alpine
RUN pip install xnat loguru

RUN mkdir /app
WORKDIR /app

ADD update-metadata.py /app
CMD ["python", "/app/update-metadata.py"]
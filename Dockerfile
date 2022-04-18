FROM python:3.9-slim-buster
WORKDIR /app
COPY ./factorial .
RUN pip3 install -r requirements.txt
CMD rm /app/local_dev.sh
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "factorial:app"]

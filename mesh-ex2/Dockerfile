FROM python:alpine3.9

RUN pip install requests flask
COPY app.py /app.py
ENTRYPOINT ["python", "app.py"]

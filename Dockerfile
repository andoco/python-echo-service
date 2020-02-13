FROM python:3.7-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY app.py /app/
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:8080", "app:app"]

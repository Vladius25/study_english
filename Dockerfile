FROM python:3.7

RUN mkdir -p /app/src
RUN mkdir -p /app/media/uploads
WORKDIR /app

COPY app /app/src/
COPY app/requirements.txt /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "--chdir", "/app/src", "--bind", ":8800", "--workers", "6", "study_english.wsgi:application"]

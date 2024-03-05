FROM python:3.9-slim

# Create a non-root user and group
RUN groupadd -r webappuser && useradd -r -g webappuser webappuser

# Set the working directory and change its ownership to the non-root user
WORKDIR /app
RUN chown webappuser:webappuser /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app.py /app/app.py

CMD gunicorn --bind 0.0.0.0:5000  app:app
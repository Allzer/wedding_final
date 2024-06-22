FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "app:app"]

FROM python:3.9-alpine

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "Lab1:app", "--host", "0.0.0.0", "--port", "8080"]


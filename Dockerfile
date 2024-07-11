FROM python:3.9-slim

WORKDIR /app

COPY search_service.py .

RUN pip install flask

EXPOSE 5002

CMD ["python", "search_service.py"]

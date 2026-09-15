FROM python:3.13-slim

WORKDIR /app

COPY order.py .

CMD ["python", "order.py"]

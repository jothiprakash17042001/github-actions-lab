FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask pytest

CMD ["python", "app.py"]
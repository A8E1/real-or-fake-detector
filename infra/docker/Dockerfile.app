FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.app.txt .
RUN pip install --no-cache-dir -r requirements.app.txt

COPY mlops/serving/ mlops/serving/

EXPOSE 8001
CMD ["uvicorn", "mlops.serving.fastapi_app:app", "--host", "0.0.0.0", "--port", "8001"]

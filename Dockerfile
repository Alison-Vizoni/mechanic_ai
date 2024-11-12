FROM python:3.12-slim

WORKDIR /mechanic_ai

RUN apt-get update \
    && apt-get install --no-install-recommends -y postgresql-client

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

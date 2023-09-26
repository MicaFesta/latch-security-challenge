FROM python:3.11.5-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 3030
CMD ["python", "main.py"]
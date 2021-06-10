FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000 5001 5002 5003
ENTRYPOINT ["python", "app.py"]
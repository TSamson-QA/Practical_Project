FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask requests
EXPOSE 5000 5001 5002 5003
ENTRYPOINT ["python", "app.py"]
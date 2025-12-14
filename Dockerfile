
FROM python:3.10
WORKDIR /app
COPY backend ./backend
RUN pip install -r backend/requirements.txt
CMD ["python","backend/app.py"]

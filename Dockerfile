FROM python:3.10

WORKDIR /usr/src/app

COPY main.py task.mp4 yolov8n_sack.pt requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]

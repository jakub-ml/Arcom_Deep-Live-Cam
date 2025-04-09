FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1 ffmpeg

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
